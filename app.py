import streamlit as st
import cv2
import numpy as np
from sklearn.cluster import KMeans
from PIL import Image

st.set_page_config(page_title="B/W Image Colorizer", layout="centered")
st.title("🎨 Black & White Image Colorizer")

uploaded_file = st.file_uploader("Upload a black and white image (jpg/png)", type=["jpg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file).convert('L')  # Convert to grayscale
    st.image(img, caption="Uploaded Image", use_column_width=True)

    num_colors = st.slider("Choose the number of colors", min_value=2, max_value=8, value=3)

    colors = []
    st.write("### Select Colors for each cluster")
    for i in range(num_colors):
        color = st.color_picker(f"Pick Color {i+1}", "#ff0000")
        colors.append(tuple(int(color.lstrip('#')[j:j+2], 16) for j in (0, 2, 4)))  # Convert HEX to RGB

    if st.button("Colorize Image"):
        gray_img = np.array(img)

        # Flatten for clustering
        pixel_values = gray_img.reshape((-1, 1))

        # KMeans clustering
        kmeans = KMeans(n_clusters=num_colors, random_state=42).fit(pixel_values)
        clustered_img = kmeans.labels_.reshape(gray_img.shape)

        # Apply chosen colors
        color_img = np.zeros((gray_img.shape[0], gray_img.shape[1], 3), dtype=np.uint8)
        for idx in range(num_colors):
            mask = (clustered_img == idx)
            color_img[mask] = colors[idx][::-1]  # Convert RGB to BGR for OpenCV

        st.image(color_img, caption="🎨 Colorized Output", use_column_width=True)

        # Download button
        result = Image.fromarray(cv2.cvtColor(color_img, cv2.COLOR_BGR2RGB))
        result.save("colorized_output.png")
        with open("colorized_output.png", "rb") as file:
            st.download_button("Download Colorized Image", file, "colorized_output.png", "image/png")

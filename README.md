# BlackWhite2Color

🎨 Black & White Image Colorizer (Streamlit App)
This project is a simple yet interactive Black & White Image Colorizer built using Streamlit, OpenCV, NumPy, and scikit-learn's KMeans Clustering. The app allows users to upload a grayscale (B/W) image and add vibrant colors to it based on selected color clusters.




 Features
 
✅ Upload any black and white image (JPG or PNG)

✅ Choose the number of color clusters (2 to 8)

✅ Select custom colors for each cluster using a color picker

✅ Automatically colorize the image based on KMeans clustering

✅ Preview the colorized image instantly

✅ Download the colorized output as a PNG file




🛠 Tech Stack
Python

Streamlit for the interactive web interface

OpenCV for image processing

NumPy for numerical operations

scikit-learn (KMeans) for clustering grayscale pixels

PIL (Pillow) for image handling and saving



Install dependencies:

pip install streamlit opencv-python numpy scikit-learn pillow


Run the Streamlit app :

streamlit run app.py

or

python -m streamlit run app.py  





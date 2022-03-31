from PIL import Image
import streamlit as st
st.title("Image Classification of select fruits and vegetables")
st.header("Image Classification of select fruits and vegetables")
st.text("Upload a clear jpg image of fruit or vegetable (only orange,banana,apple,tomato,gitter guard, capsicum")
from image_classification import machine_classification 
uploaded_file = st.file_uploader("Enter image", type=["png","jpeg","jpg"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = machine_classification(image, 'ml_model.h5')
    if label>=0 and label<=5:
        st.write("The uploaded item is fresh")
    elif label>=6 and label<=11:
        st.write("The uploaded item is rotten")
    else:
        st.write("improper image or no image uploaded")

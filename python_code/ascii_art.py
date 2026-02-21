import streamlit as st
from PIL import Image
from ascii_core import image_to_ascii

st.title("ASCII Art Generator")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)

    st.image(image, caption="Original Image", width="stretch")

    width_slider = st.slider("Output width", 50, 200, 100)
    ascii_art = image_to_ascii(image, new_width=width_slider)
    st.code(ascii_art, language=None)

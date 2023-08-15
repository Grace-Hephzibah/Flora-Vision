import streamlit as st
from PIL import Image
from helper_class import predict_class
import numpy as np 
import tensorflow as tf


# Initial Setup
cus_model = tf.keras.saving.load_model("Models/custom.keras")
cus_class = predict_class(cus_model)

tl_model = tf.keras.saving.load_model("Models/model_21.keras")
tl_class = predict_class(tl_model)

st.set_page_config( page_title= "Flora Vision", 
                   page_icon= '💐', 
                   layout='wide',
                   initial_sidebar_state='expanded'
                    )

# Side Bar
with st.sidebar:
    st.subheader("Toggle Here!")
    option = st.radio("Model", ("Custom Architecture", "Transfer Learning - ResNet50"), 
                      index = 1)
    if option == 'Custom Architecture':
        chosen_class = cus_class
    elif option == 'Transfer Learning - ResNet50':
        chosen_class = tl_class

# page title
st.markdown("<h1 style = 'text-align:center'>Flora Vision</h1>", unsafe_allow_html=True)
st.divider()

# Uploading Files 
uploads = st.file_uploader("Choose A Image File",  
                            accept_multiple_files=True, 
                            type = ['png', 'jpg', 'jpeg'])
st.divider()

# Iterating through the uploaded files
if uploads:
    for upload in uploads:
        image = Image.open(upload)
        im = tf.keras.utils.img_to_array(image)
        im = np.expand_dims(im, axis = 0)
        im = np.resize(im, (1, 150, 150, 3))
        a, b, c = st.columns(3)
        with a:
            st.image(image)
        with b:
            pred_dict = chosen_class.predict_flower(im)
            st.write(pred_dict)
        with c:
            pred_class = "### ```" + chosen_class.dict_max(pred_dict) + "```"
            st.markdown("### The Predicted Class : ")
            st.markdown(pred_class)
        st.divider()
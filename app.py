import streamlit as st
from PIL import Image
from helper_class import predict_class
import numpy as np 
import tensorflow as tf


# Initial Setup
cus_model = tf.keras.saving.load_model("Models/custom.keras")
cus_class = predict_class(cus_model)
cus_des= "#### Model - 19 : Accuracy score = ```71.92%```"

tl_model = tf.keras.saving.load_model("Models/model_21.keras")
tl_class = predict_class(tl_model)
tl_des = "#### Model - 21 : Accuracy score = ```90.38%```"



# Page setup 
st.set_page_config( page_title= "Flora Vision", 
                   page_icon= '💐', 
                   layout='wide',
                   initial_sidebar_state='expanded'
                    )
# page title
st.markdown("<h1 style = 'text-align:center'>Flora Vision</h1>", unsafe_allow_html=True)
st.divider()



# Side Bar
with st.sidebar:
    st.title("Toggle Here!")
    option_model = st.radio("What Model Do You Prefer?", ("Custom Architecture", "Transfer Learning - ResNet50"), 
                      index = 1)
    if option_model == 'Custom Architecture':
        chosen_class = cus_class
        chosen_des = cus_des
    elif option_model == 'Transfer Learning - ResNet50':
        chosen_class = tl_class
        chosen_des = tl_des
    st.write(chosen_des)

    option_type = st.radio("How Do You Want To Test?", ("Upload Your Own Images", "Random Test"), 
                      index = 1)
    if option_type == "Random Test":
        num_images = st.number_input("What's The Number Of Images?", min_value=1, max_value=20)
    st.divider()

    st.write("To check out the model code, go to the ```Github Repo/architecture/```")
    st.write("Github Link: https://github.com/Grace-Hephzibah/Flora-Vision")
    st.divider()


if option_type == "Upload Your Own Images":
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

if option_type == "Random Test":
    st.write("I am working!")

# Outro 
st.markdown("# By Grace Hephzibah ✨")
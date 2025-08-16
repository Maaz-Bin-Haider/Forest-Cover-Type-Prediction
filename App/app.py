import streamlit as st
import numpy as np
import pandas as pd
import pickle
from PIL import Image
st.set_page_config(
    page_title="Forest Cover Type Prediction",
    page_icon="🌲",
    layout="wide"
)

st.markdown("""
    <style>
        .st-emotion-cache-zy6yx3{
            width: 75%;
        }
        .forest-name {
            font-weight: bold;
            color: #27ae60;
        }
    </style>
""", unsafe_allow_html=True)

rfc_model = pickle.load(open('Model/random_forest.pkl','rb'))

st.title('Forest Cover Type Prediction')

coverIMG = Image.open('Images/CoverIMG.png')

st.image(coverIMG, caption='coverImg',use_container_width=True)

st.text('Enter all Features to Identify Cover Type')

prediction = cover_type = None

# Input
st.markdown("### Enter all Features")
st.caption("Provide comma-separated feature values (e.g. `2596,51,3,258,0,...`)")
user_input = st.text_input('features..')

if user_input:
    user_input = user_input.split(',')
    features = np.array([user_input],dtype=np.float64)
    prediction = rfc_model.predict(features).reshape(1,-1)
    prediction = int(prediction[0])
    st.write(prediction)

forests = {
    1: {'name':'Spruce/fir','image':'Images/forest01.png'},
    2: {'name':'lodgepole Pine','image':'Images/forest02.png'},
    3: {'name':'Ponderosa pine','image':'Images/forest03.png'},
    4: {'name':'Cottonwood willow','image':'Images/forest04.png'},
    5: {'name':'Aspen','image':'Images/forest05.png'},
    6: {'name':'Douglas Fir','image':'Images/forest06.png'},
    7: {'name':'Krummholz','image':'Images/forest07.png'},
}

if prediction:
    cover_type = forests.get(prediction)

if cover_type:
    name = cover_type['name']
    forest_image = cover_type['image']

    col1, col2 = st.columns([2,3])

    with col1:
        st.write("### 🌿 Predicted Cover Type")
        st.markdown(f"<p class='forest-name'>{name}</p>", unsafe_allow_html=True)

    with col2:
        displayIMG = Image.open(forest_image)
        st.image(displayIMG, caption='forest_image',use_container_width=True)



# -*- coding: utf-8 -*-

import streamlit as st
import pickle
from PIL import Image
#import tensorflow as tf
from tensorflow.keras.models import load_model
import numpy as np
#import numpy as np
#from keras.models import load_model

# Function to display the main page
def main_page():
    st.markdown("<h1 style='text-align: center; color: orange;'> Kalkulator cold basin PLTP gunung salak  </h1>", unsafe_allow_html=True)
    st.markdown('---'*10)
    
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        st.markdown("<button title='under_construction' style='cursor: not-allowed; background-color:#f0f0f0; color: gray; border: 1px solid lightgray; padding: 0.5em 1em; border-radius:5px;'>KAMOJANG</button>", unsafe_allow_html=True)
    with col2:
        st.markdown("<button title='under_construction' style='cursor: not-allowed; background-color:#f0f0f0; color: gray; border: 1px solid lightgray; padding: 0.5em 1em; border-radius:5px;'>DARAJAT</button>", unsafe_allow_html=True)
    with col3:
        st.markdown("<button title='under_construction' style='cursor: not-allowed; background-color:#f0f0f0; color: gray; border: 1px solid lightgray; padding: 0.5em 1em; border-radius:5px;'>SALAK</button>", unsafe_allow_html=True)
    with col4:
        if st.button("salak"):
            st.session_state.page = "UNIT 1"
    with col5:
        st.markdown("<button title='under_construction' style='cursor: not-allowed; background-color:#f0f0f0; color: gray; border: 1px solid lightgray; padding: 0.5em 1em; border-radius:5px;'>LAHENDONG</button>", unsafe_allow_html=True)

   
    st.markdown('---'*10)
    # Path ke file GIF
    gambar = 'gabungan.JPG'

    # Menampilkan gambar
    st.image(gambar, caption="salak's Geothermal Power Plant", use_column_width=True)
# Function to display Unit 1 page
def unit1_page():
    st.markdown("<h2 style='text-align: center;'>UNIT salak</h2>", unsafe_allow_html=True)
    st.button("BACK", on_click=back_to_main)
    
    st.markdown("<h1 style='text-align: center;'>Kalkulator Penghitung Inlet Condenser Valve </h1>", unsafe_allow_html=True)
    st.markdown('---'*10)

    def final_prediction1(values, model_unit1_regresi):
        prediction1 = model_unit1_regresi.predict([values])
        return prediction1
   
    def final_prediction2(values, model_unit1_ANN):
     values_array = np.array([values])  # Konversi list ke array NumPy
     prediction2 = model_unit1_ANN.predict(values_array)
     return prediction2

    model_unit1_regresi = pickle.load(open('kalkulator penghitung temp cold basin.pkcls.pkl', 'rb'))
    

    def main():
        initial_values = {
            "FCT 1 (A)": 190.0, 
            "FCT 2 (A)": 210.8, 
            "FCT 4 (A)": 211.9, 
            "FCT 5 (A)": 225.0, 
            "temp hot basin (C)": 48.5, 
            "tekanan cond (bara)": 0.11, 
           
        }

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                FCT_1 = st.number_input("FCT 1 (A)", value=float(initial_values["FCT 1 (A)"]), step=0.1)
            with col2:
                FCT_2 = st.number_input("FCT 2 (A)", value=float(initial_values["FCT 2 (A)"]), step=0.01)
            
               
        
        with st.container(): 
            col1, col2 = st.columns(2)
            with col1:
                FCT_4 = st.number_input("FCT 4 (A)", value=float(initial_values["FCT 4 (A)"]), step=0.1)
            with col2:
                FCT_5 = st.number_input("FCT 5 (A)", value=int(initial_values["FCT 5 (A)"]), step=1)
           
        
        with st.container(): 
            col1, col2 = st.columns(2)
            with col1:
                temp_hot_basin = st.number_input("temp hot basin (C)", value=float(initial_values["temp hot basin (C)"]), step=0.1)
            with col2:
                tekanan_cond= st.number_input("tekanan cond (bara)", value=float(initial_values["tekanan cond (bara)"]), step=0.1)
           
       
        input_values = [
            FCT_1, FCT_2, 
            FCT_4, FCT_5, temp_hot_basin,
            tekanan_cond
        ]
        
        if st.button("Prediksi1"):
            values = input_values
            Prediksi1 = final_prediction1(values, model_unit1_regresi)
            st.markdown("<h2 style='text-align: center;'>TEMP COLD BASIN</h2>", unsafe_allow_html=True)
            st.markdown(f"<h3 style='text-align: center; font-size: 3.5em;'>{Prediksi1[0]:.2f} %</h3>", unsafe_allow_html=True)
        
    
        
    
    main()

# fungsi ke halaman utama
def back_to_main():
    st.session_state.page = "main"

# kondisi halaman, jika tidak
if 'page' not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "UNIT 1":
    unit1_page()


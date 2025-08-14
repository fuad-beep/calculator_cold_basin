# -*- coding: utf-8 -*-

import streamlit as st
import pickle
import numpy as np
from PIL import Image
from tensorflow.keras.models import load_model

# ---------------------------
# Fungsi halaman utama
# ---------------------------
def main_page():
    st.markdown("<h1 style='text-align: center; color: orange;'>Kalkulator Cold Basin PLTP Gunung Salak</h1>", unsafe_allow_html=True)
    st.markdown('---' * 10)
    
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        st.markdown("<button title='under_construction' style='cursor: not-allowed; background-color:#f0f0f0; color: gray; border: 1px solid lightgray; padding: 0.5em 1em; border-radius:5px;'>KAMOJANG</button>", unsafe_allow_html=True)
    with col2:
        st.markdown("<button title='under_construction' style='cursor: not-allowed; background-color:#f0f0f0; color: gray; border: 1px solid lightgray; padding: 0.5em 1em; border-radius:5px;'>DARAJAT</button>", unsafe_allow_html=True)
    with col3:
        st.markdown("<button title='under_construction' style='cursor: not-allowed; background-color:#f0f0f0; color: gray; border: 1px solid lightgray; padding: 0.5em 1em; border-radius:5px;'>SALAK</button>", unsafe_allow_html=True)
    with col4:
        if st.button("SALAK UNIT 1"):
            st.session_state.page = "SALAK UNIT 1"
    with col5:
        st.markdown("<button title='under_construction' style='cursor: not-allowed; background-color:#f0f0f0; color: gray; border: 1px solid lightgray; padding: 0.5em 1em; border-radius:5px;'>LAHENDONG</button>", unsafe_allow_html=True)

    st.markdown('---' * 10)

    # Menampilkan gambar
    gambar = 'gabungan.JPG'
    st.image(gambar, caption="Salak's Geothermal Power Plant", use_column_width=True)


# ---------------------------
# Fungsi halaman UNIT 1
# ---------------------------
def unit1_page():
    st.markdown("<h2 style='text-align: center;'>UNIT SALAK</h2>", unsafe_allow_html=True)
    st.button("BACK", on_click=back_to_main)
    
    st.markdown("<h1 style='text-align: center;'>Kalkulator Cold Basin</h1>", unsafe_allow_html=True)
    st.markdown('---' * 10)

    # Fungsi prediksi model regresi
    def final_prediction1(values, model_unit1_regresi):
        prediction1 = model_unit1_regresi.predict([values])
        return prediction1

    # Fungsi prediksi model ANN
    def final_prediction2(values, model_unit1_ANN):
        values_array = np.array([values])
        prediction2 = model_unit1_ANN.predict(values_array)
        return prediction2

    # Load model regresi
    with open('kalkulator penghitung temp cold basin.pkcls.pkl', 'rb') as f:
        model_unit1_regresi = pickle.load(f)

    # Nilai awal input
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
            FCT_1 = st.number_input("FCT 1 (A)", value=initial_values["FCT 1 (A)"], step=0.1)
        with col2:
            FCT_2 = st.number_input("FCT 2 (A)", value=initial_values["FCT 2 (A)"], step=0.01)
    
    with st.container(): 
        col1, col2 = st.columns(2)
        with col1:
            FCT_4 = st.number_input("FCT 4 (A)", value=initial_values["FCT 4 (A)"], step=0.1)
        with col2:
            FCT_5 = st.number_input("FCT 5 (A)", value=initial_values["FCT 5 (A)"], step=1)
    
    with st.container(): 
        col1, col2 = st.columns(2)
        with col1:
            temp_hot_basin = st.number_input("Temp Hot Basin (°C)", value=initial_values["temp hot basin (C)"], step=0.1)
        with col2:
            tekanan_cond = st.number_input("Tekanan Cond (bara)", value=initial_values["tekanan cond (bara)"], step=0.1)

    # List input
    input_values = [
        FCT_1, FCT_2, 
        FCT_4, FCT_5, temp_hot_basin,
        tekanan_cond
    ]
    
    if st.button("Prediksi Cold Basin Temp"):
        Prediksi1 = final_prediction1(input_values, model_unit1_regresi)
        st.markdown("<h2 style='text-align: center;'>TEMP COLD BASIN</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; font-size: 3.5em;'>{Prediksi1[0]:.2f} °C</h3>", unsafe_allow_html=True)


# ---------------------------
# Fungsi kembali ke main
# ---------------------------
def back_to_main():
    st.session_state.page = "main"


# ---------------------------
# Routing halaman
# ---------------------------
if 'page' not in st.session_state:
    st.session_state.page = "main"

if st.session_state.page == "main":
    main_page()
elif st.session_state.page == "UNIT 1":
    unit1_page()


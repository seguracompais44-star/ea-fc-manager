import streamlit as st
import pandas as pd

st.set_page_config(page_title="Academia - Juveniles", layout="wide")

st.title("💎 Academia de Juveniles")
st.write("Seguimiento de promesas y jugadores con alto potencial.")

if 'juveniles' not in st.session_state:
    st.session_state.juveniles = []

with st.form("registro_juvenil"):
    c1, c2 = st.columns(2)
    with c1:
        nombre = st.text_input("Nombre de la Promesa")
        pos = st.text_input("Posición")
    with c2:
        potencial = st.text_input("Potencial (Ej: 85-92)")
        edad = st.number_input("Edad", 15, 18, 16)
    
    if st.form_submit_button("Registrar en Academia"):
        st.session_state.juveniles.append({"Nombre": nombre, "Posición": pos, "Potencial": potencial, "Edad": edad})
        st.success(f"{nombre} ha sido inscrito en las categorías inferiores.")

if st.session_state.juveniles:
    st.table(pd.DataFrame(st.session_state.juveniles))

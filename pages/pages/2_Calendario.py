import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calendario - EA FC 26", layout="wide")

st.title("🗓️ Calendario, Partidos y Objetivos")

tab1, tab2 = st.tabs(["Registro de Partidos", "Objetivos de la Directiva"])

with tab1:
    st.subheader("Historial de Encuentros")
    # Formulario rápido
    col1, col2, col3 = st.columns(3)
    rival = col1.text_input("Rival")
    resultado = col2.text_input("Resultado (Ej: 2-1)")
    competicion = col3.selectbox("Competición", ["Liga", "Copa", "Champions", "Amistoso"])
    
    if st.button("Registrar Partido"):
        st.success(f"Partido contra {rival} guardado.")

with tab2:
    st.subheader("Seguimiento de Temporada")
    st.checkbox("Objetivo 1: Clasificar a Europa")
    st.checkbox("Objetivo 2: Desarrollar 2 canteranos")
    st.checkbox("Objetivo 3: Mantener sueldos bajos")

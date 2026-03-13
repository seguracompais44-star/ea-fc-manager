import streamlit as st
import pandas as pd

st.header("🗓️ Calendario y Objetivos")

tab1, tab2 = st.tabs(["Partidos", "Objetivos Directiva"])

with tab1:
    st.subheader("Registro de Encuentros")
    # Lógica similar a plantilla para guardar: [Rival, Resultado, Competición]
    
with tab2:
    st.checkbox("Aumentar valor del club en un 20%")
    st.checkbox("Fichar 2 jugadores de la cantera")
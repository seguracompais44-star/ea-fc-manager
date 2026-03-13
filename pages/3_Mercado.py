import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mercado - EA FC 26", layout="wide")

st.title("💸 Mercado de Pases y Scouting")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Finanzas")
    presupuesto = st.number_input("Presupuesto (€)", value=50000000)
    gastado = st.number_input("Gastado (€)", value=0)
    st.metric("Disponible", f"{presupuesto - gastado:,} €")

with col2:
    st.subheader("Lista de Seguimiento")
    # Tabla simple de ejemplo
    df_mercado = pd.DataFrame({
        "Jugador": ["Jugador A", "Jugador B"],
        "Precio": ["20M", "15M"],
        "Interés": ["Alto", "Bajo"]
    })
    st.table(df_mercado)

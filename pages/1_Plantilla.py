import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plantilla - EA FC 26", layout="wide")

st.title("🏃 Gestión de Plantilla")

# Datos de ejemplo de tu club
datos_jugadores = {
    "Nombre": ["Mbappé", "Vinícius Jr.", "Bellingham", "Valverde"],
    "Posición": ["DC", "EI", "MC", "MC"],
    "Media": [91, 89, 88, 88],
    "Contrato": [12, 25, 7, 45],
    "Estado": ["Titular", "Titular", "Titular", "Suplente"]
}

df = pd.DataFrame(datos_jugadores)

# Filtros profesionales
col1, col2 = st.columns(2)
with col1:
    pos_filter = st.multiselect("Filtrar por Posición", options=df["Posición"].unique())
with col2:
    estado_filter = st.multiselect("Filtrar por Estado", options=df["Estado"].unique())

# Aplicar filtros
df_filtrado = df.copy()
if pos_filter:
    df_filtrado = df_filtrado[df_filtrado["Posición"].isin(pos_filter)]
if estado_filter:
    df_filtrado = df_filtrado[df_filtrado["Estado"].isin(estado_filter)]

# Mostrar tabla interactiva
st.dataframe(df_filtrado, use_container_width=True)

st.success(f"Mostrando {len(df_filtrado)} jugadores en la lista.")

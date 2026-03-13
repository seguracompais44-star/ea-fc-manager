import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plantilla - EA FC 26", layout="wide")

st.title("🏃 Gestión de Plantilla")

# Datos de tu club
datos_jugadores = {
    "Nombre": ["Mbappé", "Vinícius Jr.", "Bellingham", "Valverde"],
    "Posición": ["DC", "EI", "MC", "MC"],
    "Media": [91, 89, 88, 88],
    "Contrato": [12, 25, 7, 45],
    "Estado": ["Titular", "Titular", "Titular", "Suplente"]
}

df = pd.DataFrame(datos_jugadores)

# --- SECCIÓN DE MÉTRICAS ---
m1, m2, m3 = st.columns(3)
m1.metric("Total Jugadores", len(df))
m2.metric("Media Equipo", f"{df['Media'].mean():.1f}")
m3.metric("Contratos Totales", df['Contrato'].sum())

st.divider()

# Filtros
col1, col2 = st.columns(2)
with col1:
    pos_filter = st.multiselect("Filtrar por Posición", options=df["Posición"].unique())
with col2:
    estado_filter = st.multiselect("Filtrar por Estado", options=df["Estado"].unique())

# Lógica de filtrado
df_filtrado = df.copy()
if pos_filter:
    df_filtrado = df_filtrado[df_filtrado["Posición"].isin(pos_filter)]
if estado_filter:
    df_filtrado = df_filtrado[df_filtrado["Estado"].isin(estado_filter)]

# Mostrar tabla
st.dataframe(df_filtrado, use_container_width=True)

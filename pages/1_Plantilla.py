import streamlit as st
import pandas as pd

st.set_page_config(page_title="Plantilla - EA FC 26", layout="wide")

st.title("📋 Gestión de Plantilla y Cuerpo Técnico")

# Función para cargar o crear base de datos
def cargar_datos():
    try:
        return pd.read_csv('plantilla.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['Nombre', 'Posición', 'Media', 'Contrato'])

df = cargar_datos()

# Formulario lateral para añadir miembros
with st.sidebar.expander("Añadir Jugador/Staff"):
    nombre = st.text_input("Nombre")
    posicion = st.selectbox("Posición", ["POR", "DFC", "MC", "DC", "DT", "Prep. Físico"])
    media = st.number_input("Media (OVR)", 40, 99, 75)
    
    if st.button("Registrar"):
        nuevo = pd.DataFrame([[nombre, posicion, media, "Activo"]], columns=df.columns)
        df = pd.concat([df, nuevo], ignore_index=True)
        df.to_csv('plantilla.csv', index=False)
        st.success("Guardado")

st.subheader("Lista de Miembros")
st.dataframe(df, use_container_width=True)

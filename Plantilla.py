import streamlit as st
import pandas as pd

st.header("📋 Plantilla y Cuerpo Técnico")

# Función para cargar datos
def cargar_datos():
    try:
        return pd.read_csv('data/plantilla.csv')
    except FileNotFoundError:
        return pd.DataFrame(columns=['Nombre', 'Posición', 'Media', 'Rol'])

df_plantilla = cargar_datos()

# Formulario para añadir jugadores
with st.expander("Añadir nuevo integrante"):
    nombre = st.text_input("Nombre completo")
    pos = st.selectbox("Posición", ["POR", "DFC", "MC", "DC", "Cuerpo Técnico"])
    ovr = st.number_input("Media (OVR)", 40, 99, 75)
    
    if st.button("Guardar"):
        nuevo = pd.DataFrame([[nombre, pos, ovr, "Titular"]], columns=df_plantilla.columns)
        df_plantilla = pd.concat([df_plantilla, nuevo], ignore_index=True)
        df_plantilla.to_csv('data/plantilla.csv', index=False)
        st.success("Registrado correctamente.")

st.table(df_plantilla)
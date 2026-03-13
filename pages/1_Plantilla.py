import streamlit as st
import pandas as pd

st.set_page_config(page_title="Primer Equipo - Manager", layout="wide")

st.title("⚽ Gestión del Primer Equipo")

# Datos enfocados en Modo Carrera
if 'jugadores_primer_equipo' not in st.session_state:
    st.session_state.jugadores_primer_equipo = [
        {"Nombre": "Ejemplo Jugador", "Posición": "DC", "Media": 80, "Edad": 24, "Valor": "15M", "Estado": "Titular"}
    ]

# Formulario para inscribir jugadores
with st.expander("Inscribir nuevo jugador al Primer Equipo"):
    c1, c2, c3 = st.columns(3)
    with c1:
        nombre = st.text_input("Nombre")
        posicion = st.text_input("Posición (Ej: central, lateral)")
    with c2:
        media = st.number_input("Valoración (Media)", min_value=1, max_value=99, value=75)
        edad = st.number_input("Edad", min_value=16, max_value=45, value=22)
    with c3:
        valor = st.text_input("Valor de Mercado (Ej: 20M)")
        estado = st.selectbox("Rol", ["Titular", "Suplente", "Reserva", "Transferible"])
    
    if st.button("Añadir Jugador"):
        nuevo = {"Nombre": nombre, "Posición": posicion, "Media": media, "Edad": edad, "Valor": valor, "Estado": estado}
        st.session_state.jugadores_primer_equipo.append(nuevo)
        st.rerun()

# Tabla de plantilla
if st.session_state.jugadores_primer_equipo:
    df = pd.DataFrame(st.session_state.jugadores_primer_equipo)
    st.dataframe(df, use_container_width=True)
    
    # Métricas del equipo
    m1, m2 = st.columns(2)
    m1.metric("Media Total", f"{df['Media'].mean():.1f}")
    m2.metric("Edad Media", f"{df['Edad'].mean():.1f}")

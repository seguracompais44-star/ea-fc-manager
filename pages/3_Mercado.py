import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mercado - EA FC 26", layout="wide")

st.title("⚖️ Calculadora y Registro de Mercado")

# Inicializar el historial en la sesión si no existe
if 'historial' not in st.session_state:
    st.session_state.historial = []

with st.container():
    st.subheader("Nueva Operación")
    c1, c2, c3 = st.columns([2, 2, 1])
    
    with c1:
        jugador = st.text_input("Nombre del Jugador", placeholder="Ej: Mbappé")
    with c2:
        p_compra = st.number_input("Precio Compra", min_value=0, step=100, value=1000)
    with c3:
        p_venta = st.number_input("Precio Venta", min_value=0, step=100, value=1100)

    # Cálculos
    tax = p_venta * 0.05
    beneficio = (p_venta - tax) - p_compra

    if st.button("Añadir al Historial"):
        nueva_fila = {"Jugador": jugador, "Compra": p_compra, "Venta": p_venta, "Tax": int(tax), "Neto": int(beneficio)}
        st.session_state.historial.append(nueva_fila)
        st.success(f"Registrado: {jugador}")

st.divider()

# Mostrar el historial si tiene datos
if st.session_state.historial:
    st.subheader("📈 Historial de Hoy")
    df_historial = pd.DataFrame(st.session_state.historial)
    st.table(df_historial)
    
    # Suma total de beneficios del día
    total_dia = df_historial["Neto"].sum()
    st.metric("Beneficio Total de la Sesión", f"{total_dia} 🪙")
    
    if st.button("Limpiar Historial"):
        st.session_state.historial = []
        st.rerun()
else:
    st.info("Aún no hay operaciones registradas hoy.")

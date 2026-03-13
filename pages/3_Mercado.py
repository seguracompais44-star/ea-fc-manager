import streamlit as st
import pandas as pd

st.set_page_config(page_title="Mercado - Modo Carrera", layout="wide")

st.title("💰 Gestión de Fichajes y Presupuesto")

# Inicializar presupuesto y lista de deseos en la sesión
if 'presupuesto' not in st.session_state:
    st.session_state.presupuesto = 100000000  # 100M por defecto
if 'wishlist' not in st.session_state:
    st.session_state.wishlist = []

# --- PANEL DE CONTROL DE PRESUPUESTO ---
col_pre1, col_pre2 = st.columns(2)
with col_pre1:
    st.metric("Presupuesto Actual", f"{st.session_state.presupuesto:,} €")
with col_pre2:
    nuevo_presupuesto = st.number_input("Actualizar Presupuesto Total", value=st.session_state.presupuesto, step=1000000)
    if st.button("Guardar Nuevo Presupuesto"):
        st.session_state.presupuesto = nuevo_presupuesto
        st.rerun()

st.divider()

# --- CALCULADORA DE FICHAJE ---
st.subheader("🔎 Análisis de Posible Fichaje")
c1, c2, c3 = st.columns([2, 2, 1])

with c1:
    nombre_fichaje = st.text_input("Nombre del Objetivo")
with c2:
    coste_estimado = st.number_input("Coste del Traspaso (€)", min_value=0, step=500000)
with c3:
    st.write("¿Es viable?")
    if coste_estimado <= st.session_state.presupuesto:
        st.success("SÍ ✅")
    else:
        st.error("NO ❌")

if st.button("Añadir a Lista de Deseos"):
    st.session_state.wishlist.append({"Jugador": nombre_fichaje, "Coste": coste_estimado})
    st.rerun()

# --- LISTA DE DESEOS (WISHLIST) ---
if st.session_state.wishlist:
    st.subheader("📝 Lista de Objetivos")
    df_wish = pd.DataFrame(st.session_state.wishlist)
    st.table(df_historial)
    
    total_inversion = df_wish["Coste"].sum()
    st.warning(f"Inversión total necesaria para estos fichajes: {total_inversion:,} €")
    
    if st.button("Limpiar Lista"):
        st.session_state.wishlist = []
        st.rerun()

import streamlit as st

st.header("💸 Mercado de Pases")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Presupuesto Transferencias")
    presupuesto = st.number_input("Euros (€)", min_value=0, value=50000000)

with col2:
    st.subheader("Jugadores Objetivo")
    # Tabla interactiva para seguimiento de cláusulas y estados de negociación
import streamlit as st

st.set_page_config(page_title="Mercado - EA FC 26", layout="wide")

st.title("⚖️ Calculadora de Beneficios (Tax 5%)")

with st.container():
    st.subheader("Cálculo de Transacción")
    
    col1, col2 = st.columns(2)
    
    with col1:
        precio_compra = st.number_input("Precio de Compra (Coins)", min_value=0, step=100, value=1000)
    
    with col2:
        precio_venta = st.number_input("Precio de Venta (Coins)", min_value=0, step=100, value=2000)

    # Lógica del mercado de EA
    impuesto = precio_venta * 0.05
    recibe = precio_venta - impuesto
    beneficio = recibe - precio_compra

    st.divider()

    # Resultados
    res1, res2, res3 = st.columns(3)
    res1.metric("Impuesto EA (5%)", f"-{int(impuesto)} 🪙")
    res2.metric("Recibes tras Tax", f"{int(recibe)} 🪙")
    
    # Color dinámico para el beneficio
    if beneficio > 0:
        res3.metric("Beneficio Neto", f"+{int(beneficio)} 🪙", delta="Ganancia")
    elif beneficio < 0:
        res3.metric("Beneficio Neto", f"{int(beneficio)} 🪙", delta="Pérdida", delta_color="inverse")
    else:
        res3.metric("Beneficio Neto", "0 🪙")

st.info("Usa esta herramienta para saber si una inversión vale la pena antes de vender.")

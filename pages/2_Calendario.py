import streamlit as st
import pandas as pd

st.set_page_config(page_title="Calendario - EA FC 26", layout="wide")

st.title("📅 Calendario de Temporada")
st.write("Gestiona tus próximos partidos y eventos del club.")

# Simulación de calendario
data = {
    "Fecha": ["2026-03-15", "2026-03-18", "2026-03-22"],
    "Competición": ["Champions League", "Liga", "Copa"],
    "Rival": ["Real Madrid", "FC Barcelona", "Atlético de Madrid"],
    "Estado": ["Pendiente", "Pendiente", "Pendiente"]
}
df = pd.DataFrame(data)

st.table(df)

st.info("Próximamente: Podrás añadir resultados y notas de cada partido.")

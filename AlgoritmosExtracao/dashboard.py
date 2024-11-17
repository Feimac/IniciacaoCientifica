import streamlit as st
from streamlit.components.v1 import html
import time

# Função para exibir o mapa a partir do buffer HTML
def exibir_mapa():
    with open("mapa_buffer.html", "r", encoding="utf-8") as file:
        mapa_html = file.read()
    html(mapa_html, height=500, width=700)

# Configuração do dashboard
st.title("Dashboard de Atrasos em Tempo Real")
st.markdown("### Mapa de Calor dos Atrasos")

# Botão para recarregar o mapa
if st.button("Atualizar"):
    exibir_mapa()
else:
    st.write("Clique em 'Atualizar' para carregar o mapa de calor.")


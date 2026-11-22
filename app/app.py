import os
from datetime import datetime

import streamlit as st

FILE_PATH = os.getenv("FILE_PATH", "/data/arquivo.txt")
MAX_LINHAS = 200

st.set_page_config(page_title="Visualizador GitHub", layout="centered")
st.title("📄 Arquivo do GitHub")


# run_every reexecuta só este trecho a cada 30s, sem recarregar a página toda
@st.fragment(run_every="30s")
def mostrar_arquivo():
    if not os.path.exists(FILE_PATH):
        st.warning("O arquivo ainda não foi baixado. Aguarde o updater.")
        return

    atualizado = datetime.fromtimestamp(os.path.getmtime(FILE_PATH))
    with open(FILE_PATH, encoding="utf-8", errors="replace") as f:
        linhas = f.read().splitlines()

    col1, col2, col3 = st.columns(3)
    col1.metric("Última atualização", f"{atualizado:%H:%M:%S}")
    col2.metric("Linhas", f"{len(linhas):,}")
    col3.metric("Tamanho", f"{os.path.getsize(FILE_PATH) / 1024:.0f} KB")

    st.caption(f"Mostrando as primeiras {min(MAX_LINHAS, len(linhas))} linhas "
               f"· verificado às {datetime.now():%H:%M:%S}")
    st.code("\n".join(linhas[:MAX_LINHAS]), language="text", line_numbers=True)


mostrar_arquivo()
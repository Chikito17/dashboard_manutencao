import streamlit as st
from dataset import df_dcv

st.title('Teste Alessandro')

st.sidebar.title('Filtro:')
filtro_desc = st.sidebar.text_input('Vamos em Frente')
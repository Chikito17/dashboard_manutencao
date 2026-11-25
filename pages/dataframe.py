import streamlit as st
from dataset import df_dcv

st.title('Visão de Paradas')

st.sidebar.title('Filtro:')
filtro_desc = st.sidebar.text_input('Digite o Parâmetro')

st.dataframe(df_dcv)
import streamlit as st
from dataset import df_dcv

st.title('Visao de Paradas')

st.sidebar.title('Filtro:')

filtro_desc = st.sidebar.text_input('Digite o Parametro')


if filtro_desc:
    df_dcv = df_dcv[df_dcv['grupo'].str.contains(filtro_desc, case=False, na=False)]


st.dataframe(df_dcv)
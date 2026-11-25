import streamlit as st
from dataset import df_dcv

st.title('Visao de Paradas')

st.sidebar.title('Filtros:')
filtro_tag = st.sidebar.text_input('Digite o Parametro')


st.title('Visao de Paradas')
with st.expander('grupo'):
    colunas = st.multiselect(
        'Selecione ao Grupo',
        list(df_dcv.columns),
        list(df_dcv.columns)
    )
st.dataframe(df_dcv)
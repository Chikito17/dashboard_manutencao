import streamlit as st 
from dataset import df_rm
from dataset import df_sm
from dataset import df_dc
from dataset import df_smf

st.set_page_config(layout='wide') # Para usar toda a janela

st.title('Manutenção LTQ - AGM') # Titulo da aplicacao

st.sidebar.title('Filtros') # Essa linha cria uma aba removivel com o nome Fitros

filtro_tag = st.sidebar.text_input('Digite a tag') # Adiciona uma caixa de texto na barra lateral

if filtro_tag:
    df_rm = df_rm[df_rm['Tag'].str.contains(filtro_tag, case=False, na=False)]

aba1, aba2, aba3, aba4 = st.tabs(['Mapa de Memoria RM', 'Mapa de Memoria SM', 'Mapa de Memoria DC','Mapa de Memoria SMF'])

with aba1:
    st.dataframe(df_rm)

with aba2:
    st.dataframe(df_sm)

with aba3:
    st.dataframe(df_dc)

with aba4:
    st.dataframe(df_smf)
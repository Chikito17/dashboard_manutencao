import streamlit as st 
from dataset import df

st.set_page_config(layout='wide') # Para usar toda a janela

st.title('Manutenção LTQ - AGM') # Titulo da aplicacao

st.sidebar.title('Filtros') # Essa linha cria uma aba removivel com o nome Fitros

filtro_tag = st.sidebar.text_input('') # Adiciona uma caixa de texto na barra lateral

aba1, aba2, aba3, aba4 = st.tabs(['Mapa de Memoria RM', 'Mapa de Memoria SM', 'Mapa de Memoria DC','Mapa de Memoria SMF'])

with aba1:
    st.dataframe(df)
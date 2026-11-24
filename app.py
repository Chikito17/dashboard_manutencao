import streamlit as st 
from dataset import df

st.set_page_config(layout='wide') # Para usar toda a janela

st.title('Manutenção LTQ - AGM') # Titulo da aplicacao

st.sidebar.title('Filtros') # Essa linha cria uma aba removivel com o nome Fitros

filtro_tag = st.sidebar.text_input('') # Adiciona uma caixa de texto na barra lateral
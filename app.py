import streamlit as st 
from dataset import df_rm
from dataset import df_sm
from dataset import df_dc
from dataset import df_smf

st.set_page_config(layout='wide') # Para usar toda a janela

st.title('Manutenção LTQ - AGM') # Titulo da aplicacao

st.sidebar.title('Filtros') # Essa linha cria uma aba removivel com o nome Fitros

filtro_tag = st.sidebar.text_input('Digite a tag') # Adiciona uma caixa de texto na barra lateral
filtro_endereco = st.sidebar.text_input('Digite o Bit') 

if filtro_tag:
    filtro_endereco = ""
    df_rm = df_rm[df_rm['Tag'].str.contains(filtro_tag, case=False, na=False)]
    df_sm = df_sm[df_sm['Tag'].str.contains(filtro_tag, case=False, na=False)]
    df_dc = df_dc[df_dc['Tag'].str.contains(filtro_tag, case=False, na=False)]
    df_smf = df_smf[df_smf['Tag'].str.contains(filtro_tag, case=False, na=False)]

if filtro_endereco:
    filtro_tag = ""
    df_rm = df_rm[df_rm['SIEMENS'].str.contains(filtro_endereco, case=False, na=False)]
    df_sm = df_sm[df_sm['SIEMENS'].str.contains(filtro_endereco, case=False, na=False)]
    df_dc = df_dc[df_dc['SIEMENS'].str.contains(filtro_endereco, case=False, na=False)]
    df_smf = df_smf[df_smf['SIEMENS'].str.contains(filtro_endereco, case=False, na=False)]


    

aba1, aba2, aba3, aba4 = st.tabs(['Mapa de Memoria RM', 'Mapa de Memoria SM', 'Mapa de Memoria DC','Mapa de Memoria SMF'])

with aba1:
    st.dataframe(df_rm)

with aba2:
    st.dataframe(df_sm)

with aba3:
    st.dataframe(df_dc)

with aba4:
    st.dataframe(df_smf)
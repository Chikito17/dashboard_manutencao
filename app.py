import streamlit as st 
from dataset import df_rm
from dataset import df_sm
from dataset import df_dc
from dataset import df_smf
from dataset import df_dcv

st.set_page_config(layout='wide') # Para usar toda a janela

st.title('Manutenção LTQ - AGM') # Titulo da aplicacao

st.sidebar.title('Filtros PLC:') # Essa linha cria uma aba removivel com o nome Fitros

filtro_tag = st.sidebar.text_input('Digite a tag') # Adiciona uma caixa de texto na barra lateral
filtro_endereco = st.sidebar.text_input('Digite o Bit') 
filtro_descricao = st.sidebar.text_input('Digite a descricao') 

if filtro_tag:
    #st.session_state.filtro_endereco = "" # Nao funcionou
    df_rm = df_rm[df_rm['Tag'].str.contains(filtro_tag, case=False, na=False)]
    df_sm = df_sm[df_sm['Tag'].str.contains(filtro_tag, case=False, na=False)]
    df_dc = df_dc[df_dc['Tag'].str.contains(filtro_tag, case=False, na=False)]
    df_smf = df_smf[df_smf['Tag'].str.contains(filtro_tag, case=False, na=False)]

if filtro_endereco:
    #st.session_state.filtro_tag = "" # Nao funcionou
    df_rm = df_rm[df_rm['SIEMENS'].str.contains(filtro_endereco, case=False, na=False)]
    df_sm = df_sm[df_sm['SIEMENS'].str.contains(filtro_endereco, case=False, na=False)]
    df_dc = df_dc[df_dc['SIEMENS'].str.contains(filtro_endereco, case=False, na=False)]
    df_smf = df_smf[df_smf['SIEMENS'].str.contains(filtro_endereco, case=False, na=False)]

if filtro_descricao:
    df_rm = df_rm[df_rm['Descrição'].str.contains(filtro_descricao, case=False, na=False)]
    df_sm = df_sm[df_sm['Descrição'].str.contains(filtro_descricao, case=False, na=False)]
    df_dc = df_dc[df_dc['Descrição'].str.contains(filtro_descricao, case=False, na=False)]
    df_smf = df_smf[df_smf['Descrição'].str.contains(filtro_descricao, case=False, na=False)]

    

aba1, aba2, aba3, aba4, aba5 = st.tabs(['Rougher', 'Steckel', 'Bob. Final','Fornos SMF', 'DCV'])

with aba1:
    st.dataframe(df_rm)

with aba2:
    st.dataframe(df_sm)

with aba3:
    st.dataframe(df_dc)

with aba4:
    st.dataframe(df_smf)

with aba5:
    
    st.sidebar.title('Filtro DCV:')
    filtro_desc = st.sidebar.text_input('Digite o Parâmetro')

    # Mantém o original intacto e trabalha numa cópia
    df_filtrado = df_dcv.copy()

    if filtro_desc:
       df_filtrado = filtro_desc
       # df_filtrado = df_filtrado[
       #     df_filtrado['grupo'].astype(str).str.contains(filtro_desc, case=False, na=False)
       # ]

    st.dataframe(df_filtrado)

    # Exibe contagem de registros encontrados e a tabela
    st.caption(f"Exibindo {len(df_filtrado)} de {len(df_dcv)} registros.")
    
    
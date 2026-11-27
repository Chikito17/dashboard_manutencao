import streamlit as st
from dataset import df_dcv
from dataset import df_dcv700
import pandas as pd

st.title('Acionamentos')

#################### Codigo para os Paramentros
st.sidebar.title('Filtro DCV:')
filtro_desc = st.sidebar.text_input('Digite o Parâmetro')

# Mantém o original intacto e trabalha numa cópia
df_filtrado = df_dcv.copy()

if filtro_desc:
    df_filtrado = df_filtrado[df_filtrado['grupo'] == filtro_desc]
    



##################### Codigo para as Falhas
st.sidebar.title('Codigo de Falha:')
filtro_falha = st.sidebar.text_input('Digite o codigo')

# Mantém o original intacto e trabalha numa cópia
df_falha = df_dcv700.copy()

if filtro_falha:
    df_falha = df_falha[df_falha['Código'] == filtro_falha]
    
              
  
aba1, aba2 = st.tabs(['Parametros', 'Codigo de Falhas'])

with aba1:
    st.dataframe(df_filtrado)
    

with aba2:
      
    if not df_falha.empty:
        st.metric('Codigo', df_falha['Código'].item())
        st.subheader("Descrição da falha")
        linha = df_falha.iloc[0]
        st.write(linha["Descrição"])
        with st.expander("Procedimento de correção"):
            st.text(linha["O que fazer"])

        
        
        
       
              
    
    
  
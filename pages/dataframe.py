import streamlit as st
from dataset import df_dcv

st.title('Visão de Paradas')

st.sidebar.title('Filtro:')
filtro_desc = st.sidebar.text_input('Digite o Parâmetro')

# Mantém o original intacto e trabalha numa cópia
df_filtrado = df_dcv.copy()

if filtro_desc:
    df_filtrado = df_filtrado[
        df_filtrado['grupo'].astype(str).str.contains(filtro_desc, case=False, na=False)
    ]

#st.dataframe(df_filtrado)


# Exibe contagem de registros encontrados e a tabela
st.caption(f"Exibindo {len(df_filtrado)} de {len(df_dcv)} registros.")
st.dataframe(df_filtrado, use_container_width=True)
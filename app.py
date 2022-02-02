import streamlit as st
import pandas as pd

st.sidebar.radio(
    'Selecione uma Opção',
    ('Registro de Medalhas', 'Análise Geral', 'Análise por país', 'Análise por Atleta')
)

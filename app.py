import streamlit as st

pg = st.navigation([
    st.Page("app_cliente.py", title="Cadastro de Clientes"),
    st.Page("app_servico.py", title="Cadastro de Serviços"),
])

pg.run()
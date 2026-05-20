import streamlit as st
import datetime
from banco import criar_tabela
from cadastrar_cliente import cadastrar_cliente

criar_tabela()

st.title("Cadastro de Clientes")

if st.session_state.get("cadastrado"):
    st.success("Cliente cadastrado com sucesso!")
    st.session_state["cadastrado"] = False

if "data_cadastro" not in st.session_state:
    st.session_state["data_cadastro"] = datetime.date.today()

with st.form("form_cadastro", clear_on_submit=True):
    nome = st.text_input("Nome")
    endereco = st.text_input("Endereço")

    codigo_cliente = st.number_input(
        "Código",
        min_value=1,
        step=1,
        format="%d"
    )

    cnpj = st.text_input("CNPJ", max_chars=18)
    cidade = st.text_input("Cidade", max_chars=100)
    estado = st.text_input("Estado", max_chars=2)
    email = st.text_input("E-mail", max_chars=100)
    telefone = st.text_input("Telefone", max_chars=20)

    data_cadastro = st.date_input(
        "Escolha a data de cadastro",
        min_value=datetime.date(1900, 1, 1),
        max_value=datetime.date.today(),
        value=st.session_state["data_cadastro"]
    )

    cadastrar = st.form_submit_button("Cadastrar Cliente")

if cadastrar:
    try:
        cadastrar_cliente(
            nome,
            endereco,
            int(codigo_cliente),
            cnpj,
            cidade,
            estado,
            email,
            telefone,
            data_cadastro
        )

        st.session_state["cadastrado"] = True
        st.session_state["data_cadastro"] = datetime.date.today()
        st.rerun()

    except Exception as e:
        st.error(f"Erro ao cadastrar cliente: {e}")
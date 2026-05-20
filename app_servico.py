import streamlit as st
import datetime
from banco import criar_tabela
from cadastrar_servico import cadastrar_servico

criar_tabela()

st.title("Cadastro de Serviços")

if st.session_state.get("cadastrado"):
    st.success("Serviço cadastrado com sucesso!")
    st.session_state["cadastrado"] = False

if "data_inicial" not in st.session_state:
    st.session_state["data_inicial"] = datetime.date.today()

if "data_final" not in st.session_state:
    st.session_state["data_final"] = datetime.date.today()    

with st.form("form_cadastro", clear_on_submit=True):
    codigo_cliente = st.number_input("Código Cliente",
                                        min_value=1,
                                        step=1,
                                        format="%d"
                                    )
    data_inicial = st.date_input("Escolha a data inicial",
                                    min_value=datetime.date(1900, 1, 1),
                                    max_value=datetime.date.today(),
                                    value=st.session_state["data_inicial"]
                                )
    data_final = st.date_input("Escolha a data final",
                                    min_value=datetime.date(1900, 1, 1),
                                    max_value=datetime.date.today(),
                                    value=st.session_state["data_final"]
                                )    
    desc_rat = st.text_input("Descrição RAT", max_chars=100)
    desc_serv = st.text_input("Descrição Serviço", max_chars=999)
    sit_serv = st.selectbox("Situação",["Em Andamento",
                            "Aguardando Aprovação",
                            "Aprovado"])

    cadastrar = st.form_submit_button("Cadastrar Serviço")

if cadastrar:
    try:
        cadastrar_servico(
            int(codigo_cliente),
            data_inicial,
            data_final,
            desc_rat,
            desc_serv,
            sit_serv
        )

        st.session_state["cadastrado"] = True
        st.session_state["data_inicial"] = datetime.date.today()
        st.session_state["data_final"] = datetime.date.today()        
        st.rerun()

    except Exception as e:
        st.error(f"Erro ao cadastrar serviço: {e}")
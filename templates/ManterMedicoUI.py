import streamlit as st
import pandas as pd
from views import View
import time

class ManterMedicoUI:
    def main():
        st.header("Cadastro de médicos")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterMedicoUI.listar()
        with tab2:
            ManterMedicoUI.inserir()
        with tab3:
            ManterMedicoUI.atualizar()
        with tab4:
            ManterMedicoUI.excluir()

    def listar():
        medicos = View.medico_listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            list_dic = []
            for obj in medicos:
                list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome")
        especialidade = st.text_input("Informe a especialidade")
        conselho = st.text_input("Informe o conselho")
        email = st.text_input("Informe o email")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            View.medico_inserir(nome, especialidade, conselho, email, senha)
            st.success("Médico inserido com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        medicos = View.medico_listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            op = st.selectbox("Atualização de médicos", medicos)
            nome = st.text_input("Informe o novo nome", op.get_nome())
            especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
            conselho = st.text_input("Informe o novo conselho", op.get_conselho())
            email = st.text_input("Informe o novo email", op.get_email())
            senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
            if st.button("Atualizar"):
                id = op.get_id()
                View.medico_atualizar(id, nome, especialidade, conselho, email, senha)
                st.success("Médico atualizado com sucesso")
                time.sleep(2)
                st.rerun()

    def excluir():
        medicos = View.medico_listar()
        if len(medicos) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            op = st.selectbox("Exclusão de médicos", medicos)
            if st.button("Excluir"):
                id = op.get_id()
                View.medico_excluir(id)
                st.success("Médico excluído com sucesso")
                time.sleep(2)
                st.rerun()
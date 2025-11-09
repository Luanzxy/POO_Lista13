import streamlit as st
import pandas as pd
from views import View
import time

class ManterPacienteUI:
    def main():
        st.header("Cadastro de Pacientes")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1: ManterPacienteUI.listar()
        with tab2: ManterPacienteUI.inserir()
        with tab3: ManterPacienteUI.atualizar()
        with tab4: ManterPacienteUI.excluir()

    def listar():
        pacientes = View.paciente_listar()
        if len(pacientes) == 0: st.write("Nenhum paciente cadastrado")
        else:
            list_dic = []
            for obj in pacientes: list_dic.append(obj.to_json())
            df = pd.DataFrame(list_dic)
            st.dataframe(df, hide_index=True)

    def inserir():
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            try:
                View.paciente_inserir(nome, email, fone, senha)
                st.success("Paciente inserido com sucesso")
            except ValueError as erro:
                st.error(erro)
            time.sleep(2)
            st.rerun()

    def atualizar():
        pacientes = View.paciente_listar()
        if len(pacientes) == 0: st.write("Nenhum paciente cadastrado")
        else:
            op = st.selectbox("Atualização de Pacientes", pacientes)
            nome = st.text_input("Novo nome", op.get_nome())
            email = st.text_input("Novo e-mail", op.get_email())
            fone = st.text_input("Novo fone", op.get_fone())
            senha = st.text_input("Nova senha", op.get_senha(), type="password")
            if st.button("Atualizar"):
                try:
                    id = op.get_id()
                    View.paciente_atualizar(id, nome, email, fone, senha)
                    st.success("Paciente atualizado com sucesso")
                except ValueError as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()


    def excluir():
        pacientes = View.paciente_listar()
        if len(pacientes) == 0: st.write("Nenhum paciente cadastrado")
        else:
            op = st.selectbox("Exclusão de Pacientes", pacientes)
            if st.button("Excluir"):
                try:
                    id = op.get_id()
                    View.paciente_excluir(id)
                    st.success("Paciente excluído com sucesso")
                except Exception as erro:
                    st.error(erro)
                time.sleep(2)
                st.rerun()
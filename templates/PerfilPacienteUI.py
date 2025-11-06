import streamlit as st
from views import View
import time

class PerfilPacienteUI:
    def main():
        st.header("Meus Dados")
        op = View.paciente_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        fone = st.text_input("Informe o novo fone", op.get_fone())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        data_nascimento = st.text_input("Informe a nova data de nascimento (DD-MM-AAAA)", op.get_data_nascimento())
        if st.button("Atualizar"):
            id = op.get_id()
            View.medico_atualizar(id, nome, email, fone, senha, data_nascimento)
            st.success("Paciente atualizado com sucesso")
            time.sleep(2)
            st.rerun()
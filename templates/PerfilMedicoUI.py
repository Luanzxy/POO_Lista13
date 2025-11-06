import streamlit as st
from views import View
import time

class PerfilMedicoUI:
    def main():
        st.header("Meus Dados")
        op = View.medico_listar_id(st.session_state["usuario_id"])
        nome = st.text_input("Informe o novo nome", op.get_nome())
        email = st.text_input("Informe o novo e-mail", op.get_email())
        especialidade = st.text_input("Informe a nova especialidade", op.get_especialidade())
        conselho = st.text_input("Informe o novo conselho", op.get_conselho())
        senha = st.text_input("Informe a nova senha", op.get_senha(), type="password")
        data_nascimento = st.text_input("Informe a nova data de nascimento (DD-MM-AAAA)", op.get_data_nascimento())
        if st.button("Atualizar"):
            id = op.get_id()
            View.profissional_atualizar(id, nome, especialidade, conselho, email, senha, data_nascimento)
            st.success("Médico atualizado com sucesso")
            time.sleep(2)
            st.rerun()

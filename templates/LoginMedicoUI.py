import streamlit as st
from views import View

class LoginMedicoUI:
    def main():
        st.header("Entrar no Sistema de médicos")
        email = st.text_input("Informe o e-mail")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Entrar"):
            p = View.medico_autenticar(email, senha)
            if p == None: st.write("E-mail ou senha inválidos")
            else:
                st.session_state["usuario_id"] = p["id"]
                st.session_state["usuario_nome"] = p["nome"]
                st.rerun()
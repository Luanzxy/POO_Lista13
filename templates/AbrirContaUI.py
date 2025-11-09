import streamlit as st
from views import View
import time

class AbrirContaUI:
    def main():
        st.header("Abrir Conta no Sistema")
        nome = st.text_input("Informe o nome")
        email = st.text_input("Informe o e-mail")
        fone = st.text_input("Informe o fone")
        senha = st.text_input("Informe a senha", type="password")
        if st.button("Inserir"):
            try:
                if nome == "":
                    st.error("O nome é obrigatório!")
                    return
                if email == "": 
                    st.error("O e-mail é obrigatório!")
                    return
                if fone == "": 
                    st.error("O fone é obrigatório!")
                    return
                if senha == "": 
                    st.error("A senha é obrigatória!")
                    return
                View.paciente_inserir(nome, email, fone, senha)
                st.success("Conta criada com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Não foi possível criar a conta: {e}")
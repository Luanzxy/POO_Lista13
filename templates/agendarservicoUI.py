import streamlit as st
from views import View
import time

class AgendarServicoUI:
    def main():
        st.header("Agendar Serviço")
        profs = View.profissional_listar()
        if len(profs

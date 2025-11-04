from templates.ManterClienteUI import ManterClienteUI
from templates.ManterServicoUI import ManterServicoUI
from templates.ManterHorarioUI import ManterHorarioUI
from templates.ManterProfissionalUI import ManterProfissionalUI
from templates.AlterarSenhaUI import AlterarSenhaUI
from templates.AbrirContaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.LoginProfissionalUI import LoginProfissionalUI
from templates.PerfilClienteUI import PerfilClienteUI
from templates.PerfilProfissionalUI import PerfilProfissionalUI
from templates.AgendarServicoUI import AgendarServicoUI
from templates.VisualizarAgendaUI import VisualizarAgendaUI
from templates.VisualizarServicoUI import VisualizarServicoUI
from templates.ConfirmarServicoUI import ConfirmarServicoUI
from views import View
import streamlit as st

class IndexUI:
    def main():
        View.cliente_criar_admin()
        IndexUI.sidebar()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Entrar no Sistema de profissionais", "Abrir Conta"])
        if op == "Entrar no Sistema":
            LoginUI.main()
        if op == "Entrar no Sistema de profissionais":
            LoginProfissionalUI.main()
        if op == "Abrir Conta":
            AbrirContaUI.main()

    def menu_cliente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Serviço", "Meus Serviços"])
        if op == "Meus Dados":
            PerfilClienteUI.main()
        if op == "Agendar Serviço":
            AgendarServicoUI.main()
        if op == "Meus Serviços":
            VisualizarAgendaUI.main()

    def menu_profissional():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "gerenciar agenda", "confirmar serviço"])
        if op == "Meus Dados":
            PerfilProfissionalUI.main()
        if op == "gerenciar agenda":
            VisualizarAgendaUI.main()
        if op == "confirmar serviço":
            ConfirmarServicoUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Clientes", "Cadastro de Serviços", "Cadastro de Horários", "Cadastro de Profissionais", "Alterar Senha"])
        if op == "Cadastro de Clientes":
            ManterClienteUI.main()
        if op == "Cadastro de Serviços":
            ManterServicoUI.main()
        if op == "Cadastro de Horários":
            ManterHorarioUI.main()
        if op == "Cadastro de Profissionais":
            ManterProfissionalUI.main()
        if op == "Alterar Senha":
            AlterarSenhaUI.main()

    def sair_do_sistema():
        if st.sidebar.button("Sair"):
            del st.session_state["usuario_id"]
            del st.session_state["usuario_nome"]
            st.rerun()

    def sidebar():
        if "usuario_id" not in st.session_state:
            IndexUI.menu_visitante()
        else:
            admin = st.session_state["usuario_nome"] == "admin"
            profissional = (
                not admin and View.profissional_listar_id(st.session_state["usuario_id"]) is not None
            )
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin:
                IndexUI.menu_admin()
            elif profissional:
                IndexUI.menu_profissional()
            else:
                IndexUI.menu_cliente()
            IndexUI.sair_do_sistema()

IndexUI.main()
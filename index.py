from templates.ManterPacienteUI import ManterPacienteUI
from templates.ManterConsultaUI import ManterConsultaUI
from templates.ManterHorarioUI import ManterHorarioUI
from templates.ManterMedicoUI import ManterMedicoUI
from templates.AlterarSenhaUI import AlterarSenhaUI
from templates.AbrirContaUI import AbrirContaUI
from templates.loginUI import LoginUI
from templates.LoginMedicoUI import LoginMedicoUI
from templates.PerfilPacienteUI import PerfilPacienteUI
from templates.PerfilMedicoUI import PerfilMedicoUI
from templates.AgendarConsultaUI import AgendarConsultaUI
from templates.VisualizarAgendaUI import VisualizarAgendaUI
from templates.VisualizarConsultaUI import VisualizarConsultaUI
from templates.ConfirmarConsultaUI import ConfirmarConsultaUI
from templates.PrescreverMedicamentoUI import PrescreverMedicamentoUI
from views import View
import streamlit as st

class IndexUI:
    def main():
        View.paciente_criar_admin()
        IndexUI.sidebar()

    def menu_visitante():
        op = st.sidebar.selectbox("Menu", ["Entrar no Sistema", "Entrar no Sistema dos Médicos", "Abrir Conta"])
        if op == "Entrar no Sistema":
            LoginUI.main()
        if op == "Entrar no Sistema dos Médicos":
            LoginMedicoUI.main()
        if op == "Abrir Conta":
            AbrirContaUI.main()

    def menu_paciente():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "Agendar Consulta", "Minhas Consultas"])
        if op == "Meus Dados":
            PerfilPacienteUI.main()
        if op == "Agendar Consulta":
            AgendarConsultaUI.main()
        if op == "Minhas Consultas":
            VisualizarAgendaUI.main()

    def menu_medico():
        op = st.sidebar.selectbox("Menu", ["Meus Dados", "visualizar agenda", "confirmar consulta", "Prescrever Medicamento"])
        if op == "Meus Dados":
            PerfilMedicoUI.main()
        if op == "visualizar agenda":
            VisualizarAgendaUI.main()
        if op == "confirmar consulta":
            ConfirmarConsultaUI.main()
        if op == "Prescrever Medicamento":
            PrescreverMedicamentoUI.main()

    def menu_admin():
        op = st.sidebar.selectbox("Menu", ["Cadastro de Pacientes", "Cadastro de Consultas", "Cadastro de Horários", "Cadastro de Médicos", "Alterar Senha"])
        if op == "Cadastro de Pacientes":
            ManterPacienteUI.main()
        if op == "Cadastro de Consultas":
            ManterConsultaUI.main()
        if op == "Cadastro de Horários":
            ManterHorarioUI.main()
        if op == "Cadastro de Médicos":
            ManterMedicoUI.main()
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
            medico = (
                not admin and View.medico_listar_id(st.session_state["usuario_id"]) is not None
            )
            st.sidebar.write("Bem-vindo(a), " + st.session_state["usuario_nome"])
            if admin:
                IndexUI.menu_admin()
            elif medico:
                IndexUI.menu_medico()
            else:
                IndexUI.menu_paciente()
            IndexUI.sair_do_sistema()

IndexUI.main()
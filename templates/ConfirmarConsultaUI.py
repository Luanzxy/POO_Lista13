import streamlit as st
import time
from views import View

class ConfirmarConsultaUI:
    def main():
        st.header("Confirmar Serviço")

        medico = View.medico_listar_id(st.session_state["usuario_id"])
        if medico is None:
            st.warning("Nenhum médico logado.")
            return

        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return

        horarios_medico = [
            h for h in horarios
            if h.get_id_medico() == medico.get_id() and h.get_id_paciente() is not None
        ]
        if len(horarios_medico) == 0:
            st.info("Você não possui horários agendados com pacientes.")
            return

        op = st.selectbox(
            "Informe o horário",
            horarios_medico,
            format_func=lambda h: f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')} - {h.get_confirmado()}"
        )

        paciente = View.paciente_listar_id(op.get_id_paciente())
        pacientes_op = []
        if paciente is not None:
            pacientes_op.append(paciente)

        paciente_selecionado = st.selectbox("Paciente", pacientes_op,
                                            format_func=lambda c: f"{c.get_id()} - {c.get_nome()} - {c.get_email()} - {c.get_fone()}")

        if st.button("Confirmar"):
            View.horario_atualizar(
                op.get_id(),
                op.get_data(),
                True,
                op.get_id_paciente(),
                op.get_id_consulta(),
                op.get_id_medico()
            )
            st.success("Consulta confirmado com sucesso!")
            time.sleep(2)
            st.rerun()
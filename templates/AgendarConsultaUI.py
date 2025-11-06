import streamlit as st
from views import View
import time

class AgendarConsultaUI:
    def main():
        st.header("Agendar Consulta")
        meds = View.medico_listar()
        if len(meds) == 0:
            st.write("Nenhum médico cadastrado")
        else:
            medico = st.selectbox("Informe o médico", meds)
            horarios = View.horario_agendar_horario(medico.get_id())
            if len(horarios) == 0:
                st.write("Nenhum horário disponível")
            else:
                horario = st.selectbox("Informe o horário", horarios)
                consultas = View.consulta_listar()
                consulta = st.selectbox("Informe a consulta", consultas)

                if st.button("Agendar"):
                    View.horario_atualizar(
                        horario.get_id(),
                        horario.get_data(),
                        False,
                        st.session_state["usuario_id"],
                        consulta.get_id(),
                        medico.get_id()
                    )
                    st.success("Horário agendado com sucesso")
                    time.sleep(2)
                    st.rerun()
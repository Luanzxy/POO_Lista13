import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime, date

class VisualizarAgendaUI:
    def main():
        st.header("Agenda")
        tab1, tab2 = st.tabs(["Listar", "Inserir"])
        with tab1:
            VisualizarAgendaUI.listar()
        with tab2:
            VisualizarAgendaUI.inserir()

    def listar():
        medico = View.medico_listar_id(st.session_state["usuario_id"])
        if medico is None:
            st.warning("Nenhum médico logado.")
            return

        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return

        horarios_medico = [h for h in horarios if h.get_id_profissional() == medico.get_id()]
        if len(horarios_medico) == 0:
            st.info("Você ainda não abriu horários na sua agenda.")
            return

        dic = []
        for obj in horarios_medico:
            paciente = View.paciente_listar_id(obj.get_id_paciente())
            consulta = View.consulta_listar_id(obj.get_id_consulta())
            dic.append({
                "id": obj.get_id(),
                "data": obj.get_data(),
                "confirmado": obj.get_confirmado(),
                "paciente": paciente.get_nome() if paciente else None,
                "consulta": consulta.get_descricao() if consulta else None
            })

        df = pd.DataFrame(dic)
        st.dataframe(df, hide_index=True)

    def inserir():
        medico = View.medico_listar_id(st.session_state["usuario_id"])
        if medico is None:
            st.warning("Nenhum médico logado.")
            return

        data = st.date_input("Informe o dia do atendimento", date.today())
        hora_inicial = st.time_input("Hora inicial do atendimento")
        hora_final = st.time_input("Hora final do atendimento")
        intervalo = st.number_input("Intervalo entre atendimentos (em minutos)", min_value=5, step=5)

        if st.button("Gerar horários"):
            from datetime import datetime, timedelta
            inicio = datetime.combine(data, hora_inicial)
            fim = datetime.combine(data, hora_final)
            horarios_gerados = []

            while inicio < fim:
                View.horario_inserir(inicio, False, None, None, medico.get_id())
                horarios_gerados.append(inicio.strftime("%H:%M"))
                inicio += timedelta(minutes=intervalo)

            st.success(f"Foram inseridos {len(horarios_gerados)} horários na agenda!")
            time.sleep(2)
            st.rerun()

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

        def _get_prof_id(h):
            for name in ("get_id_profissional", "get_id_medico", "get_profissional_id", "get_medico_id"):
                attr = getattr(h, name, None)
                if callable(attr):
                    try:
                        return attr()
                    except Exception:
                        continue
                elif attr is not None:
                    return attr
            for name in ("id_profissional", "id_medico", "profissional_id", "medico_id"):
                if hasattr(h, name):
                    return getattr(h, name)
            for rel in ("profissional", "medico"):
                obj = getattr(h, rel, None)
                if obj:
                    getid = getattr(obj, "get_id", None)
                    if callable(getid):
                        try:
                            return getid()
                        except Exception:
                            pass
                    if hasattr(obj, "id"):
                        return getattr(obj, "id")
            return None

        horarios_medico = [h for h in horarios if _get_prof_id(h) == medico.get_id()]
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

            if inicio >= fim:
                st.error("A hora inicial deve ser anterior à hora final.")
                return

            intervalo = int(intervalo)
            horarios_gerados = []
            horarios_falhos = []

            while inicio < fim:
                try:
                    res = View.horario_inserir(inicio, False, None, None, medico.get_id())
                    if res is False or res is None:
                        horarios_falhos.append(inicio.strftime("%H:%M"))
                    else:
                        horarios_gerados.append(inicio.strftime("%H:%M"))
                except Exception as e:
                    horarios_falhos.append(inicio.strftime("%H:%M"))
                inicio += timedelta(minutes=intervalo)

            if len(horarios_gerados) > 0:
                st.success(f"Foram inseridos {len(horarios_gerados)} horários: {', '.join(horarios_gerados)}")
            if len(horarios_falhos) > 0:
                st.warning(f"Falha ao inserir {len(horarios_falhos)} horários: {', '.join(horarios_falhos)}")

            time.sleep(1)
            st.rerun()

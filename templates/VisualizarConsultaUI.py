import streamlit as st
import pandas as pd
from views import View

class VisualizarConsultaUI:
    def main():
        st.header("Minhas Consultas")
        paciente = View.paciente_listar_id(st.session_state["usuario_id"])
        if paciente is None:
            st.warning("Nenhum paciente logado.")
            return

        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.info("Nenhum horário cadastrado.")
            return

        horarios_paciente = [h for h in horarios if h.get_id_paciente() == paciente.get_id()]
        if len(horarios_paciente) == 0:
            st.info("Você ainda não possui consultas agendadas.")
            return

        dic = []
        for obj in horarios_paciente:
            consulta = View.consulta_listar_id(obj.get_id_consulta())
            medico = View.medico_listar_id(obj.get_id_medico())
            dic.append({
                "id": obj.get_id(),
                "data": obj.get_data(),
                "confirmado": obj.get_confirmado(),
                "consulta": consulta.get_descricao() if consulta else None,
                "médico": medico.get_nome() if medico else None
            })

        df = pd.DataFrame(dic)
        st.dataframe(df, hide_index=True)

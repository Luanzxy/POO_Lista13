import streamlit as st
import pandas as pd
from views import View
import time
from datetime import datetime

class ManterHorarioUI:
    def main():
        st.header("Cadastro de Horários")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterHorarioUI.listar()
        with tab2:
            ManterHorarioUI.inserir()
        with tab3:
            ManterHorarioUI.atualizar()
        with tab4:
            ManterHorarioUI.excluir()

    def listar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            dic = []
            for obj in horarios:
                paciente = View.paciente_listar_id(obj.get_id_paciente())
                consulta = View.consulta_listar_id(obj.get_id_consulta())
                medico = View.medico_listar_id(obj.get_id_medico())
                paciente_nome = paciente.get_nome() if paciente != None else None
                medico_nome = medico.get_nome() if medico != None else None
                consulta_desc = consulta.get_descricao() if consulta != None else None
                dic.append({
                    "id": obj.get_id(),
                    "data": obj.get_data().strftime("%d/%m/%Y %H:%M") if obj.get_data() else None,
                    "confirmado": obj.get_confirmado(),
                    "paciente": paciente_nome,
                    "consulta": consulta_desc,
                    "medico": medico_nome
                })
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    def inserir():
        pacientes = View.paciente_listar()
        consultas = View.consulta_listar()
        medicos = View.medico_listar()
        data = st.text_input("Informe a data e horário da consulta", datetime.now().strftime("%d/%m/%Y %H:%M"))
        confirmado = st.checkbox("Confirmado")
        paciente = st.selectbox("Informe o paciente", pacientes, index=None)
        medico = st.selectbox("Informe o médico", medicos, index=None)
        consulta = st.selectbox("Informe a consulta", consultas, index=None)

        if st.button("Inserir"):
            id_paciente = None
            id_consulta = None
            id_medico = None
            if paciente != None: id_paciente = paciente.get_id()
            if medico != None: id_medico = medico.get_id()
            if consulta != None: id_consulta = consulta.get_id()
            try:
                dt = datetime.strptime(data, "%d/%m/%Y %H:%M")
                View.horario_inserir(dt, confirmado, id_paciente, id_consulta, id_medico)
                st.success("Horário inserido com sucesso")
                time.sleep(2)
                st.rerun()
            except Exception as e:
                st.error(f"Erro ao inserir horário: {e}")

    def atualizar():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            pacientes = View.paciente_listar()
            medicos = View.medico_listar()
            consultas = View.consulta_listar()
            op = st.selectbox("Atualização de Horários", horarios)

            data = st.text_input("Informe a nova data e horário da consulta", op.get_data().strftime("%d/%m/%Y %H:%M") if op.get_data() else "")
            confirmado = st.checkbox("Nova confirmação", op.get_confirmado())

            id_paciente = None if op.get_id_paciente() in [0, None] else op.get_id_paciente()
            id_medico = None if op.get_id_medico() in [0, None] else op.get_id_medico()
            id_consulta = None if op.get_id_consulta() in [0, None] else op.get_id_consulta()

            paciente = st.selectbox("Informe o novo paciente", pacientes, next((i for i, c in enumerate(pacientes) if c.get_id() == id_paciente), None))
            medico = st.selectbox("Informe o novo médico", medicos, next((i for i, m in enumerate(medicos) if m.get_id() == id_medico), None))
            consulta = st.selectbox("Informe a nova consulta", consultas, next((i for i, s in enumerate(consultas) if s.get_id() == id_consulta), None))

            if st.button("Atualizar"):
                id_paciente = None
                id_medico = None
                id_consulta = None
                if paciente != None: id_paciente = paciente.get_id()
                if medico != None: id_medico = medico.get_id()
                if consulta != None: id_consulta = consulta.get_id()
                try:
                    dt = datetime.strptime(data, "%d/%m/%Y %H:%M")
                    View.horario_atualizar(op.get_id(), dt, confirmado, id_paciente, id_consulta, id_medico)
                    st.success("Horário atualizado com sucesso")
                except Exception as e:
                    st.error(f"Erro ao atualizar horário: {e}")

    def excluir():
        horarios = View.horario_listar()
        if len(horarios) == 0:
            st.write("Nenhum horário cadastrado")
        else:
            op = st.selectbox("Exclusão de Horários", horarios)
            if st.button("Excluir"):
                View.horario_excluir(op.get_id())
                st.success("Horário excluído com sucesso")
                time.sleep(2)
                st.rerun()
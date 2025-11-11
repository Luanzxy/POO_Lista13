import streamlit as st
from views import View
from datetime import datetime
import time

class PrescreverMedicamentoUI:
    def main():
        st.header("Prescrever Medicamento")

        medico_id = st.session_state.get("usuario_id", None)
        if medico_id is None:
            st.warning("Faça login como médico para acessar esta tela.")
            return

        agora = datetime.now()
        horarios = [h for h in View.horario_listar() if h.get_id_medico() == medico_id
                    and h.get_data() is not None and h.get_data() <= agora and h.get_id_paciente() not in [0, None]]

        if not horarios:
            st.info("Nenhuma consulta passada encontrada para este médico.")
            return

        def fmt(h):
            paciente = View.paciente_listar_id(h.get_id_paciente())
            paciente_nome = paciente.get_nome() if paciente else "Paciente desconhecido"
            return f"{h.get_id()} - {h.get_data().strftime('%d/%m/%Y %H:%M')} - {paciente_nome}"

        op = st.selectbox("Selecione a consulta / atendimento", horarios, format_func=fmt)

        paciente = View.paciente_listar_id(op.get_id_paciente())
        st.markdown(f"**Paciente:** {paciente.get_nome() if paciente else '—'}")
        st.markdown(f"**Data da consulta:** {op.get_data().strftime('%d/%m/%Y %H:%M') if op.get_data() else '—'}")

        medicamento = st.text_input("Medicamento (nome)")
        dosagem = st.text_input("Dosagem (ex.: 1 comprimido, 12/12h)")
        instrucoes = st.text_area("Instruções (ex.: por quantos dias, observações)")

        if st.button("Prescrever"):
            try:
                if not medicamento.strip():
                    st.error("Informe o medicamento.")
                else:
                    View.prescricao_inserir(
                        medico_id,
                        op.get_id_paciente(),
                        op.get_id(),
                        medicamento.strip(),
                        dosagem.strip(),
                        instrucoes.strip(),
                        datetime.now()
                    )
                    st.success("Prescrição registrada com sucesso.")
                    time.sleep(1)
                    st.rerun()
            except Exception as e:
                st.error(f"Erro ao registrar prescrição: {e}")
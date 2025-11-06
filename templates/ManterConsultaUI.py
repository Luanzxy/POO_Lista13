import streamlit as st
import pandas as pd
import time
from views import View

class ManterConsultaUI:

    def main():
        st.header("Cadastro de Consultas")
        tab1, tab2, tab3, tab4 = st.tabs(["Listar", "Inserir", "Atualizar", "Excluir"])
        with tab1:
            ManterConsultaUI.listar()
        with tab2:
            ManterConsultaUI.inserir()
        with tab3:
            ManterConsultaUI.atualizar()
        with tab4:
            ManterConsultaUI.excluir()

    def listar():
        consultas = View.consulta_listar()
        if len(consultas) == 0:
            st.write("Nenhuma consulta cadastrada")
        else:
            dic = []
            for obj in consultas:
                dic.append({
                    "id": obj.get_id(),
                    "descricao": obj.get_descricao(),
                    "valor": obj.get_valor()
                })
            df = pd.DataFrame(dic)
            st.dataframe(df, hide_index=True)

    def inserir():
        descricao = st.text_input("Descrição do serviço")
        valor = st.number_input("Valor do serviço", min_value=0.0, step=0.1)
        if st.button("Inserir"):
            View.consulta_inserir(descricao, valor)
            st.success("Consulta inserida com sucesso")
            time.sleep(2)
            st.rerun()

    def atualizar():
        consultas = View.consulta_listar()
        if len(consultas) == 0:
            st.write("Nenhuma consulta cadastrada")
        else:
            op = st.selectbox("Atualização de Consultas", consultas)
            descricao = st.text_input("Nova descrição", op.get_descricao())
            valor = st.number_input("Novo valor", value=op.get_valor())
            if st.button("Atualizar"):
                id = op.get_id()
                View.consulta_atualizar(id, descricao, valor)
                st.success("Consulta atualizada com sucesso")
                st.rerun()

    def excluir():
        consultas = View.consulta_listar()
        if len(consultas) == 0:
            st.write("Nenhuma consulta cadastrada")
        else:
            op = st.selectbox("Exclusão de Consultas", consultas)
            if st.button("Excluir"):
                id = op.get_id()
                View.consulta_excluir(id)
                st.success("Consulta excluída com sucesso")
                time.sleep(2)
                st.rerun()

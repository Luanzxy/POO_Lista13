from models.consulta import Consulta, ConsultaDAO
from models.paciente import Paciente, PacienteDAO
from models.horarios import Horario, HorarioDAO
from models.medico import Medico, MedicoDAO
from datetime import datetime, date

class View:
    def paciente_inserir(nome, email, fone, senha, data_nascimento=None):
        paciente = Paciente(0, nome, email, fone, senha, data_nascimento)
        PacienteDAO.inserir(paciente)

    def paciente_listar():
        return PacienteDAO.listar()

    def paciente_listar_id(id):
        return PacienteDAO.listar_id(id)

    def paciente_atualizar(id, nome, email, fone, senha, data_nascimento=None):
        paciente = Paciente(id, nome, email, fone, senha, data_nascimento)
        PacienteDAO.atualizar(paciente)

    def paciente_excluir(id):
        paciente = Paciente(id, "", "", "", "")
        PacienteDAO.excluir(paciente)

    def paciente_criar_admin():
        for p in View.paciente_listar():
            if p.get_email() == "admin":
                return
        View.paciente_inserir("admin", "admin", "fone", "1234")

    def paciente_autenticar(email, senha):
        for p in View.paciente_listar():
            if p.get_email() == email and p.get_senha() == senha:
                return {"id": p.get_id(), "nome": p.get_nome()}
        return None

    def medico_inserir(nome, especialidade, conselho, email, senha, data_nascimento=None):
        medico = Medico(0, nome, especialidade, conselho, email, senha, data_nascimento)
        MedicoDAO.inserir(medico)

    def medico_listar():
        return MedicoDAO.listar()

    def medico_listar_id(id):
        return MedicoDAO.listar_id(id)

    def medico_atualizar(id, nome, especialidade, conselho, email, senha, data_nascimento=None):
        medico = Medico(id, nome, especialidade, conselho, email, senha, data_nascimento)
        MedicoDAO.atualizar(medico)

    def medico_excluir(id):
        medico = Medico(id, "", "", "", "", "")
        MedicoDAO.excluir(medico)

    def medico_autenticar(email, senha):
        for m in View.medico_listar():
            if m.get_email() == email and m.get_senha() == senha:
                return {"id": m.get_id(), "nome": m.get_nome()}
        return None

    def consulta_listar():
        return ConsultaDAO.listar()

    def consulta_listar_id(id):
        return ConsultaDAO.listar_id(id)

    def consulta_inserir(descricao, valor):
        consulta = Consulta(0, descricao, valor)
        ConsultaDAO.inserir(consulta)

    def consulta_atualizar(id, descricao, valor):
        consulta = Consulta(id, descricao, valor)
        ConsultaDAO.atualizar(consulta)

    def consulta_excluir(id):
        consulta = Consulta(id, "", 0.0)
        ConsultaDAO.excluir(consulta)

    def horario_inserir(data, confirmado, id_paciente, id_consulta, id_medico):
        c = Horario(0, data)
        c.set_confirmado(confirmado)
        c.set_id_paciente(id_paciente)
        c.set_id_consulta(id_consulta)
        c.set_id_medico(id_medico)
        HorarioDAO.inserir(c)

    def horario_listar():
        return HorarioDAO.listar()

    def horario_atualizar(id, data, confirmado, id_paciente, id_consulta, id_medico):
        c = Horario(id, data)
        c.set_confirmado(confirmado)
        c.set_id_paciente(id_paciente)
        c.set_id_consulta(id_consulta)
        c.set_id_medico(id_medico)
        HorarioDAO.atualizar(c)

    def horario_excluir(id):
        c = Horario(id, None)
        HorarioDAO.excluir(c)

    def horario_agendar_horario(id_medico):
        r = []
        agora = datetime.now()
        for h in View.horario_listar():
            if (
                h.get_data() is not None and
                h.get_data() >= agora and
                h.get_confirmado() == False and
                h.get_id_paciente() == None and
                h.get_id_medico() == id_medico
            ):
                r.append(h)
        r.sort(key=lambda h: h.get_data())
        return r
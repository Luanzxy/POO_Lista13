from models.cliente import Cliente, ClienteDAO
from models.servico import Servico, ServicoDAO
from models.horarios import Horario, HorarioDAO
from models.profissional import Profissional, ProfissionalDAO

class View:
    @staticmethod
    def cliente_autenticar(email, senha):
        for c in View.cliente_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return{"id": c.get_id(), "nome": c.get_nome()}
        return None
    
    @staticmethod
    def profissional_autenticar(email, senha):
        for c in View.profissional_listar():
            if c.get_email() == email and c.get_senha() == senha:
                return{"id": c.get_id(), "nome": c.get_nome()}
        return None

    @staticmethod
    def cliente_criar_admin():
        for c in View.cliente_listar():
            if c.get_email() == "admin": return
            View.cliente_inserir("admin", "admin", "fone", "1234")

    @staticmethod
    def cliente_listar():
        return ClienteDAO.listar()

    @staticmethod
    def cliente_inserir(nome, email, fone, senha):
        cliente = Cliente(0, nome, email, fone, senha)
        ClienteDAO.inserir(cliente)

    @staticmethod
    def cliente_atualizar(id, nome, email, fone, senha):
        cliente = Cliente(id, nome, email, fone, senha)
        ClienteDAO.atualizar(cliente)

    @staticmethod
    def cliente_excluir(id):
        cliente = Cliente(id, "", "", "")
        ClienteDAO.excluir(cliente)

    @staticmethod
    def servico_listar():
        return ServicoDAO.listar()

    @staticmethod
    def servico_inserir(descricao,valor):
        servico = Servico(0, descricao,valor)
        ServicoDAO.inserir(servico)

    @staticmethod
    def servico_atualizar(id, descricao,valor):
        servico = Servico(id, descricao,valor)
        ServicoDAO.atualizar(servico)

    @staticmethod
    def servico_excluir(id):
        servico= Servico(id, "", 0)
        ServicoDAO.excluir(servico)

    @staticmethod
    def horario_inserir(data, confirmado, id_cliente, id_servico, id_profissional):
        horario = Horario(0, data)
        horario.set_confirmado(confirmado)
        horario.set_id_cliente(id_cliente)
        horario.set_id_servico(id_servico)
        horario.set_id_profissional(id_profissional)

        HorarioDAO.inserir(horario)

    @staticmethod
    def horario_listar():
        return HorarioDAO.listar()

    @staticmethod
    def horario_atualizar(id, data, confirmado, id_cliente, id_servico, id_profissional):
        horario = Horario(id, data)
        horario.set_confirmado(confirmado)
        horario.set_id_cliente(id_cliente)
        horario.set_id_servico(id_servico)
        horario.set_id_profissional(id_profissional)

        HorarioDAO.atualizar(horario)

    @staticmethod
    def horario_excluir(id):
        horario = HorarioDAO.listar_id(id)
        if horario:
            HorarioDAO.excluir(horario)

    @staticmethod
    def profissional_listar():
        return ProfissionalDAO.listar()

    @staticmethod
    def profissional_inserir(nome, especialidade, conselho, email, senha):
        profissional = Profissional(0, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.inserir(profissional)

    @staticmethod
    def profissional_atualizar(id, nome, especialidade, conselho, email, senha):
        profissional = Profissional(id, nome, especialidade, conselho, email, senha)
        ProfissionalDAO.atualizar(profissional)

    @staticmethod
    def profissional_excluir(id):
        profissional = Profissional(id, "", "", "")
        ProfissionalDAO.excluir(profissional)                    
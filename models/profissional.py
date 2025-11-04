import json
from models.dao import DAO

class Profissional:
    def __init__(self, id, nome, especialidade, conselho, email, senha):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.conselho = conselho
        self.email = email
        self.senha = senha

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_especialidade(self): return self.especialidade
    def get_email(self): return self.email
    def get_senha(self): return self.senha

    def set_id(self, id): self.id = id
    def set_nome(self, nome): self.nome = nome
    def set_especialidade(self, especialidade): self.especialidade = especialidade
    def set_conselho(self, conselho): self.conselho = conselho
    def set_email(self, email): self.email = email
    def set_senha(self, senha): self.senha = senha

    def to_json(self):
        dic = {
            "id": self.id,
            "nome": self.nome,
            "especialidade": self.especialidade,
            "conselho": self.conselho,
            "email": self.email,
            "senha": self.senha
        }
        return dic

    @staticmethod
    def from_json(dic):
        return Profissional(dic["id"], dic["nome"], dic["especialidade"],
                           dic["conselho"], dic["email"], dic["senha"])

    def __str__(self):
        return f"{self.id} - {self.nome} - {self.especialidade} - {self.conselho} - {self.email} - {self.senha}"


class ProfissionalDAO:

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("profissional.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Profissional.from_json(dic)
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("profissional.json", mode="w") as arquivo:
            json.dump([o.to_json() for o in cls.objetos], arquivo)

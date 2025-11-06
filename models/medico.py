import json
from models.dao import DAO
from datetime import date

class Medico:
    def __init__(self, id, nome, especialidade, conselho, email, senha, data_nascimento=None):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.conselho = conselho
        self.email = email
        self.senha = senha
        self.set_data_nascimento(data_nascimento)

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_especialidade(self): return self.especialidade
    def get_email(self): return self.email
    def get_senha(self): return self.senha
    def get_data_nascimento(self): return self.data_nascimento

    def set_id(self, id): self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self.__nome = nome
    def set_especialidade(self, especialidade):
        if especialidade == "": raise ValueError("Especialidade inválida")
        self.__especialidade = especialidade
    def set_conselho(self, conselho):
        if conselho == "": raise ValueError("Conselho inválido")
        self.__conselho = conselho
    def set_email(self, email):
        if email == "": raise ValueError("Email inválido")
        self.__email = email
    def set_senha(self, senha):
        if senha == "": raise ValueError("Senha inválida")
        self.__senha = senha

    def set_data_nascimento(self, data_nascimento):
        if data_nascimento == "" or data_nascimento is None:
            self._data_nascimento = ""
            return
        try:
            date.strptime(data_nascimento, "%d-%m-%Y")
            self._data_nascimento = data_nascimento
        except Exception:
            raise ValueError("Data de nascimento inválida (use o formato DD-MM-AAAA)")

    def to_json(self):
        dic = {
            "id": self.id,
            "nome": self.nome,
            "especialidade": self.especialidade,
            "conselho": self.conselho,
            "email": self.email,
            "senha": self.senha,
            "data_nascimento": self.data_nascimento
        }
        return dic

    @staticmethod
    def from_json(dic):
        return Medico(dic["id"], dic["nome"], dic["especialidade"],
                     dic["conselho"], dic["email"], dic["senha"],
                     dic.get("data_nascimento", ""))

    def __str__(self):
        dn = self.data_nascimento if self.data_nascimento else "N/D"
        return f"{self.id} - {self.nome} - {self.especialidade} - {self.conselho} - {self.email} - {dn}"


class MedicoDAO(DAO):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("medicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Medico.from_json(dic)
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("medicos.json", mode="w") as arquivo:
            json.dump([o.to_json() for o in cls.objetos], arquivo)
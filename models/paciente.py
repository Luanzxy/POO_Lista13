import json
from models.dao import DAO
from datetime import date

class Paciente:
    def __init__(self, id, nome, email, fone, senha, date):
        self.set_id(id)
        self.set_nome(nome)
        self.set_email(email)
        self.set_fone(fone)
        self.set_senha(senha)
        self.set_data_nascimento(date)
        

    def get_id(self): return self.id
    def get_nome(self): return self.nome
    def get_email(self): return self.email
    def get_fone(self): return self.fone
    def get_senha(self): return self.senha
    def get_data_nascimento(self): return self.data_nascimento

    def set_senha(self, senha):
        if senha == "": raise ValueError("Senha inválida")
        self.__senha = senha
    def set_id(self, id): self.__id = id
    def set_nome(self, nome):
        if nome == "": raise ValueError("Nome inválido")
        self.__nome = nome
    def set_email(self, email):
        if email == "": raise ValueError("Email inválido")
        self.__email = email
    def set_fone(self, fone):
        if fone == "": raise ValueError("Telefone inválido")
        self.__fone = fone

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
            "email": self.email,
            "fone": self.fone,
            "senha": self.senha,
            "data_nascimento": self.data_nascimento
        }
        return dic

    @staticmethod
    def from_json(dic):
        return Paciente(dic["id"], dic["nome"], dic["email"], dic["fone"], dic["senha"],
                       dic.get("data_nascimento", ""))

    def __str__(self):
        dn = self.data_nascimento if self.data_nascimento else "N/D"
        return f"{self.id} - {self.nome} - {self.email} - {self.fone} - {dn}"


class PacienteDAO(DAO):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("pacientes.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Paciente.from_json(dic)
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("pacientes.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Paciente.to_json)
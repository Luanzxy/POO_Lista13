import json
from models.dao import DAO

class Servico:
    def __init__(self, id, descricao, valor):
        self.set_id(id)
        self.set_descricao(descricao)
        self.set_valor(valor)

    def __str__(self):
        return f"{self.id} - {self.descricao} - R$ {self.valor:.2f}"
    
    def get_id(self): 
        return self.id
    def get_descricao(self): 
        return self.descricao
    def get_valor(self): 
        return self.valor
    
    def set_id(self, id): 
        self.id = id
    def set_descricao(self, descricao): 
        self.descricao = descricao
    def set_valor(self, valor): 
        self.valor = valor

    def to_json(self):
        dic = {
            "id": self.id,
            "descricao": self.descricao,
            "valor": self.valor
        }
        return dic

    @staticmethod
    def from_json(dic):
        return Servico(dic["id"], dic["descricao"], dic["valor"])


class ServicoDAO:

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("servicos.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Servico.from_json(dic)
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("servicos.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Servico.to_json)

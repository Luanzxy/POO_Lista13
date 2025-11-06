from datetime import datetime
import json
from models.dao import DAO

class Horario:
    def __init__(self, id, data, hora):
        self.set_id(id)
        self.set_data(data)
        self.set_hora(hora)
        self.set_id_paciente(0)
        self.set_id_consulta(0)
        self.set_id_medico(0)

    def __str__(self):
        return f"{self.id} - {self.data} {self.hora} - Paciente: {self.id_paciente} - Consulta: {self.id_consulta} - Medico: {self.id_medico}"

    def get_id(self): 
       return self.id
    def get_data(self): 
        return self.data
    def get_hora(self): 
        return self.hora
    def get_id_paciente(self): 
        return self.id_paciente
    def get_id_consulta(self): 
        return self.id_consulta
    def get_id_medico(self): 
        return self.id_medico

    def set_id(self, id): self.__id = id
    def set_data(self, data):
        if not isinstance(data, datetime):
            raise ValueError("Data inválida")
        if data.year < 2025:
            raise ValueError("Data anterior ao ano de 2025 não é permitida")
        self.__data = data
    def set_hora(self, hora): self.__hora = hora
    def set_id_paciente(self, id_paciente): self.id_paciente = id_paciente
    def set_id_consulta(self, id_consulta): self.id_consulta = id_consulta
    def set_id_medico(self, id_medico): self.id_medico = id_medico

    def to_json(self):
        dic = {
            "id": self.id,
            "data": self.data,
            "hora": self.hora,
            "id_paciente": self.id_paciente,
            "id_consulta": self.id_consulta,
            "id_medico": self.id_medico

        }
        return dic

    @staticmethod
    def from_json(dic):
        return Horario(dic["id"], dic["data"], dic["hora"], dic["id_paciente"], dic["id_consulta"], dic["id_medico"])


class HorarioDAO(DAO):

    @classmethod
    def abrir(cls):
        cls.objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    cls.objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horarios.json", mode="w") as arquivo:
            json.dump(cls.objetos, arquivo, default=Horario.to_json)
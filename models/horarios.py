from datetime import datetime
from models.dao import DAO
import json

class Horario:
    def __init__(self, id, data):
        self.set_id(id)
        self.set_data(data)
        self.set_confirmado(False)
        self.set_id_paciente(0)
        self.set_id_consulta(0)
        self.set_id_medico(0)

    def __str__(self):
        return f"{self.__id} - {self.__data.strftime('%d/%m/%Y %H:%M')} - {self.__confirmado}"

    def get_id(self): return self.__id
    def get_data(self): return self.__data
    def get_confirmado(self): return self.__confirmado
    def get_id_paciente(self): return self.__id_paciente
    def get_id_consulta(self): return self.__id_consulta
    def get_id_medico(self): return self.__id_medico

    def set_id(self, id): self.__id = id
    def set_data(self, data):
        if not isinstance(data, datetime):
            raise ValueError("Data inválida")
        if data.year < 2025:
            raise ValueError("Data anterior ao ano de 2025 não é permitida")
        self.__data = data
    def set_confirmado(self, confirmado): self.__confirmado = confirmado
    def set_id_paciente(self, id_paciente): self.__id_paciente = id_paciente
    def set_id_consulta(self, id_consulta): self.__id_consulta = id_consulta
    def set_id_medico(self, id_medico): self.__id_medico = id_medico

    def to_json(self):
        dic = {
            "id": self.__id,
            "data": self.__data.strftime("%d/%m/%Y %H:%M"),
            "confirmado": self.__confirmado,
            "id_paciente": self.__id_paciente,
            "id_consulta": self.__id_consulta,
            "id_medico": self.__id_medico
        }
        return dic

    @staticmethod
    def from_json(dic):
        horario = Horario(dic["id"], datetime.strptime(dic["data"], "%d/%m/%Y %H:%M"))
        horario.set_confirmado(dic["confirmado"])
        horario.set_id_paciente(dic["id_paciente"])
        horario.set_id_consulta(dic["id_consulta"])
        horario.set_id_medico(dic["id_medico"])
        return horario


class HorarioDAO(DAO):
    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("horarios.json", mode="r") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Horario.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            pass

    @classmethod
    def salvar(cls):
        with open("horarios.json", mode="w") as arquivo:
            json.dump(cls._objetos, arquivo, default=Horario.to_json)
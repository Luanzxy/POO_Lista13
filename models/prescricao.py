import json
from datetime import datetime
from models.dao import DAO

class Prescricao:
    def __init__(self, id, id_medico, id_paciente, id_consulta, medicamento, dosagem, instrucoes, data):
        self.set_id(id)
        self.set_id_medico(id_medico)
        self.set_id_paciente(id_paciente)
        self.set_id_consulta(id_consulta)
        self.set_medicamento(medicamento)
        self.set_dosagem(dosagem)
        self.set_instrucoes(instrucoes)
        self.set_data(data)

    def get_id(self): return self.__id
    def get_id_medico(self): return self.__id_medico
    def get_id_paciente(self): return self.__id_paciente
    def get_id_consulta(self): return self.__id_consulta
    def get_medicamento(self): return self.__medicamento
    def get_dosagem(self): return self.__dosagem
    def get_instrucoes(self): return self.__instrucoes
    def get_data(self): return self.__data

    def set_id(self, id): self.__id = id
    def set_id_medico(self, id_medico): self.__id_medico = id_medico
    def set_id_paciente(self, id_paciente): self.__id_paciente = id_paciente
    def set_id_consulta(self, id_consulta): self.__id_consulta = id_consulta
    def set_medicamento(self, medicamento):
        if medicamento is None: medicamento = ""
        self.__medicamento = medicamento
    def set_dosagem(self, dosagem):
        if dosagem is None: dosagem = ""
        self.__dosagem = dosagem
    def set_instrucoes(self, instrucoes):
        if instrucoes is None: instrucoes = ""
        self.__instrucoes = instrucoes
    def set_data(self, data):
        if isinstance(data, str):
            try:
                data = datetime.fromisoformat(data)
            except:
                data = None
        self.__data = data

    def to_json(self):
        return {
            "id": self.get_id(),
            "id_medico": self.get_id_medico(),
            "id_paciente": self.get_id_paciente(),
            "id_consulta": self.get_id_consulta(),
            "medicamento": self.get_medicamento(),
            "dosagem": self.get_dosagem(),
            "instrucoes": self.get_instrucoes(),
            "data": self.get_data().isoformat() if self.get_data() else None
        }

    @staticmethod
    def from_json(dic):
        data = dic.get("data")
        dt = None
        if data:
            try:
                dt = datetime.fromisoformat(data)
            except:
                dt = None
        return Prescricao(dic.get("id", 0),
                         dic.get("id_medico"),
                         dic.get("id_paciente"),
                         dic.get("id_consulta"),
                         dic.get("medicamento"),
                         dic.get("dosagem"),
                         dic.get("instrucoes"),
                         dt)


class PrescricaoDAO(DAO):

    @classmethod
    def abrir(cls):
        cls._objetos = []
        try:
            with open("prescricoes.json", mode="r", encoding="utf-8") as arquivo:
                list_dic = json.load(arquivo)
                for dic in list_dic:
                    obj = Prescricao.from_json(dic)
                    cls._objetos.append(obj)
        except FileNotFoundError:
            cls._objetos = []

    @classmethod
    def salvar(cls):
        with open("prescricoes.json", mode="w", encoding="utf-8") as arquivo:
            list_dic = [obj.to_json() for obj in cls._objetos]
            json.dump(list_dic, arquivo, indent=4, ensure_ascii=False)
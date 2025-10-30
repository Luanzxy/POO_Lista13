import json

class Horario:
    def __init__(self, id, data, hora, id_cliente, id_servico):
        self.set_id(id)
        self.set_data(data)
        self.set_hora(hora)
        self.set_id_cliente(id_cliente)
        self.set_id_servico(id_servico)

    def __str__(self):
        return f"{self.id} - {self.data} {self.hora} - Cliente: {self.id_cliente} - Serviço: {self.id_servico}"

    def get_id(self): 
       return self.id
    def get_data(self): 
        return self.data
    def get_hora(self): 
        return self.hora
    def get_id_cliente(self): 
        return self.id_cliente
    def get_id_servico(self): 
        return self.id_servico

    def set_id(self, id): 
        self.id = id
    def set_data(self, data): 
        self.data = data
    def set_hora(self, hora): 
        self.hora = hora
    def set_id_cliente(self, id_cliente): 
        self.id_cliente = id_cliente
    def set_id_servico(self, id_servico): 
        self.id_servico = id_servico

    def to_json(self):
        dic = {
            "id": self.id,
            "data": self.data,
            "hora": self.hora,
            "id_cliente": self.id_cliente,
            "id_servico": self.id_servico
        }
        return dic

    @staticmethod
    def from_json(dic):
        return Horario(dic["id"], dic["data"], dic["hora"], dic["id_cliente"], dic["id_servico"])


class HorarioDAO:
    objetos = []

    @classmethod
    def inserir(cls, obj):
        cls.abrir()
        id = 0
        for aux in cls.objetos:
            if aux.get_id() > id:
                id = aux.get_id()
        obj.set_id(id + 1)
        cls.objetos.append(obj)
        cls.salvar()

    @classmethod
    def listar(cls):
        cls.abrir()
        return cls.objetos

    @classmethod
    def listar_id(cls, id):
        cls.abrir()
        for obj in cls.objetos:
            if obj.get_id() == id:
                return obj
        return None

    @classmethod
    def atualizar(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.objetos.append(obj)
            cls.salvar()

    @classmethod
    def excluir(cls, obj):
        aux = cls.listar_id(obj.get_id())
        if aux is not None:
            cls.objetos.remove(aux)
            cls.salvar()

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

from enum import Enum

class Setor(Enum):
    ENGENHARIA=("Engenharia")
    JURIDICO=("Juridico")
    RECURSOS_HUMANOS=("Recursos Humanos")
    MARKETING=("Marketing")
    OPERACOES=("Operações")

    def __init__(self,nome) -> None:
        self.nome=nome
        
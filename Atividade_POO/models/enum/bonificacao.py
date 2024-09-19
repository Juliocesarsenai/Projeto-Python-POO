from enum import Enum

class Bonificacao(Enum):
    GERENTE=(0.35)
    DIRETOR=(0.45)

    def __init__(self,valor) -> None:
        self.valor=valor
        

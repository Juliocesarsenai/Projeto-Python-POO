from enum import Enum

class Sexo(Enum):
    MASCULINO=("Masculino","M")
    FEMININO=("Feminino","F")

    def __init__(self,genero,sigladogenero) -> None:
        self.genero=genero
        self.sigladogenero=sigladogenero
        
from enum import Enum

class UnidadeFederativa(Enum):
    BAHIA=("Bahia","BA")
    SAO_PAULO=("São Paulo","SP")
    RIO_DE_JANEIRO=("Rio de Janeiro","RJ")

    def __init__(self,estado,sigladoestado) -> None:
        self.estado=estado
        self.sigla=sigladoestado
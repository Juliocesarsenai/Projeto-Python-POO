from abc import ABC,abstractmethod
from Atividade_POO.models.enum.setor import Setor
from Atividade_POO.models.enum.sexo import Sexo
from Atividade_POO.models.Classes.endereco import Endereco



class Funcionario(ABC):
    def __init__(self,nome:str,cpf:str,rg:str,endereco:Endereco,setor:Setor,sexo:Sexo,salario:float,dataNascimento:str) -> None:
        self.nome=nome
        self.cpf=cpf
        self.rg=rg
        self.endereco=endereco
        self.setor=setor
        self.sexo=sexo
        self.salario=salario
        self.dataNascimento=dataNascimento

    @abstractmethod
    def getSalariofinal(self):
        pass

    def __str__(self) -> str:
        return (f"\n\t=====DADOS DO FUNCIONÁRIO=======\n\t \n\tNOME: {self.nome}"
                f"\n\tCPF: {self.cpf}"
                f"\n\tRG: {self.rg}"
                f"\n\tSETOR: {self.setor.nome}"
                f"\n\tSEXO: {self.sexo.genero}"
                f"\n\tSALÁRIO: {self.salario}"
                f"\n\tDATA DE NASCIMENTO: {self.dataNascimento}"
                f"{self.endereco}")
    
class Advogado(Funcionario):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, dataNascimento: str,oab:str) -> None:
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, dataNascimento)
        self.oab=oab
    
    def __str__(self) -> str:
        return (f"{super().__str__()} \n\tOAB:{self.oab}")

class Motorista(Funcionario):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, dataNascimento: str,cnh) -> None:
        super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, dataNascimento)
        self.cnh=cnh
    
    def __str__(self) -> str:
        return (f"{super().__str__()} \n\tCNH:{self.cnh}")
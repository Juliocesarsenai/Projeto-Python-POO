from abc import ABC,abstractmethod
from Atividade_POO.models.Classes.Funcionario import Funcionario
from Atividade_POO.models.Classes.endereco import Endereco
from Atividade_POO.models.enum.setor import Setor
from Atividade_POO.models.enum.sexo import Sexo
from Atividade_POO.models.enum.bonificacao import Bonificacao


class CargodeConfianca(Funcionario,ABC):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, dataNascimento: str,bonificacao:Bonificacao) -> None:
      super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, dataNascimento)

      self.bonificacao=bonificacao

    def __str__(self) -> str:
       return (f"{super().__str__()} \n\tBONIFICACÃO:{self.bonificacao.valor}")


class Gerente(CargodeConfianca):
    def getSalariofinal(self):
       self.salario+=self.salario*Bonificacao.GERENTE
       return self.salario
      
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, dataNascimento: str, bonificacao: Bonificacao) -> None:
       super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, dataNascimento, bonificacao)

    def __str__(self) -> str:
       return super().__str__()

class Diretor(CargodeConfianca):
    def __init__(self, nome: str, cpf: str, rg: str, endereco: Endereco, setor: Setor, sexo: Sexo, salario: float, dataNascimento: str, bonificacao: Bonificacao,premio:float) -> None:
       super().__init__(nome, cpf, rg, endereco, setor, sexo, salario, dataNascimento, bonificacao)
       
       self.premio=premio

    def __str__(self) -> str:
       return (f"{super().__str__()} \n\tPremio: {self.premio}")
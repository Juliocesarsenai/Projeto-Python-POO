from abc import ABC,abstractmethod

class Funcionario(ABC):
    def __init__(self,nome:str,cpf:str,rg:str,endereco:Endereco,setor:Setor,sexo:Sexo,salario:double,dataNascimento:str) -> None:
        self.nome=nome
        self.cpf=cpf
        self.rg=rg
        self.endereco=endereco
        self.setor=setor
        self.sexo=sexo
        self.salario=salario
        self.dataNascimento=dataNascimento

    def __str__(self) -> str:
        return (f"\nNOME: {self.nome}"
                f"\nCPF: {self.cpf}"
                f"\nRG: {self.rg}"
                f"\nSetor: {self.setor}"
                f"\nSexo: {self.sexo}"
                f"\nSalário: {self.salario}"
                f"\nData de Nascimento: {self.dataNascimento}")
from Atividade_POO.models.enum.uf import UnidadeFederativa
class Endereco:
    def __init__(self,logradouro:str,numero:str,complemento:str,cep:str,cidade:str,uf:UnidadeFederativa) -> None:
        self.logradouro=logradouro
        self.numero=numero
        self.complemento=complemento
        self.cep=cep
        self.cidade=cidade
        self.uf=uf

    def __str__(self) -> str:
        return (f"\n\n\t======DADOS DO ENDEREÇO======\n\t\n\tLOGRADOURO:{self.logradouro}"
                f"\n\tNÚMERO: {self.numero}"
                f"\n\tCOMPLEMENTO:{self.complemento}"
                f"\n\tCEP:{self.cep}"
                f"\n\tCIDADE: {self.cidade}"
                f"\n\tUNIDADE FEDERATIVA: {self.uf.estado}")
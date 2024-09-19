class Endereco:
    def __init__(self,logradouro:str,numero:str,complemento:str,cep:str,cidade:str,uf:UnidadeFederativa) -> None:
        self.logradouro=logradouro
        self.numero=numero
        self.complemento=complemento
        self.cep=cep
        self.cidade=cidade
        self.uf=uf

    def __str__(self) -> str:
        return (f"\nLOGRADOURO:{self.logradouro}"
                f"\nNÚMERO: {self.numero}"
                f"\nCOMPLEMENTO:{self.complemento}"
                f"\nCEP:{self.cep}"
                f"\nCIDADE: {self.cidade}"
                f"\nUNIDADE FEDERATIVA: {self.uf}")
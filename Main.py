from Atividade_POO.models.Classes.Funcionario import Advogado,Motorista
from Atividade_POO.models.Classes.endereco import Endereco
from Atividade_POO.models.enum.setor import Setor
from Atividade_POO.models.enum.sexo import Sexo
from Atividade_POO.models.enum.uf import UnidadeFederativa
from Atividade_POO.models.Classes.cargodeconfianca import Gerente
from Atividade_POO.models.enum.bonificacao import Bonificacao


endereco1=Endereco("Ribeira","54","Largo do Bonfim","8237831","Salvador",UnidadeFederativa.BAHIA)
endereco2=Endereco("Rua Reinaldo Bezerra","103","41","2342331","Salvador",UnidadeFederativa.BAHIA)
endereco3=Endereco("Pernambués","982","67","22399321","Salvador",UnidadeFederativa.BAHIA)
advogado=Advogado("Erick Resch","293912392","2989832",endereco1,Setor.JURIDICO,Sexo.MASCULINO,10000,"14/08/2003","238488231")
motorista=Motorista("Julio Cesar","293389843","1239213",endereco2,Setor.MARKETING,Sexo.MASCULINO,3000,"14/03/2005","128737812738")
gerente=Gerente("Julia Vales","2003903","3236342",endereco3,Setor.OPERACOES,Sexo.FEMININO,150000,"16/03/2005",Bonificacao.GERENTE)

print (advogado)
print(motorista)
print(gerente.getSalariofinal())

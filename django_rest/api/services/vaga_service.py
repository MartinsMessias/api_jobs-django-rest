from ..models import Vaga
from .tecnologia_services import listar_tecnologia_id
def listar_vagas():
    vagas = Vaga.objects.all()
    return vagas

def cadastrar_vaga(vaga):
    vaga_bd = Vaga.objects.create(titulo=vaga.titulo, descricao=vaga.descricao, salario=vaga.salario,
                                  tipo_contratacao=vaga.tipo_contratacao, local=vaga.local, quantidade=vaga.quantidade,
                                  contato=vaga.contato)
    vaga_bd.save()
    for i in vaga.tecnologias:
        tecnologia = listar_tecnologia_id(i.id)
        vaga_bd.tecnologias.add(tecnologia)
    return vaga_bd
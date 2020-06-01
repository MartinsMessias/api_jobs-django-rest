from django.http import Http404

from ..models import Tecnologia


def listar_tecnologias():
    tecnologias = Tecnologia.objects.all()
    return tecnologias


def cadastrar_tecnologia(tecnologia):
    return Tecnologia.objects.create(nome=tecnologia.nome)


def listar_tecnologia_id(id):
    try:
        return Tecnologia.objects.get(id=id)
    except Tecnologia.DoesNotExist:
        raise Http404

from ..models import Tecnologia


def listar_tecnologias():
    tecnologias = Tecnologia.objects.all()
    return tecnologias

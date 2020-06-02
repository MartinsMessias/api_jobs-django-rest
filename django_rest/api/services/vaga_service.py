from ..models import Vaga

def listar_vagas():
    vagas = Vaga.objects.all()
    return vagas

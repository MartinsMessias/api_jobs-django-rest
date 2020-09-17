from django.urls import path
from .views import tecnologia_view, vaga_view, usuario_view

from rest_framework.schemas import get_schema_view

from django.conf.urls import url
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title="Dev Jobs API")

urlpatterns = [
    url(r'^$', schema_view),
    path('tecnologias/', tecnologia_view.TecnologiaList.as_view(), name='tecnologia_list'),
    path('tecnologias/<int:id>', tecnologia_view.TecnolgiaDetalhes.as_view(), name='tecnologia_detalhes'),
    path('vagas/', vaga_view.VagaList.as_view(), name='vaga_list'),
    path('vagas/<int:id>', vaga_view.VagaDetalhes.as_view(), name='vaga_detalhes'),
    path('usuarios/', usuario_view.UsuarioList.as_view(), name='usuario_list'),
]
from django.urls import path
from .views import tecnologia_view, vaga_view

urlpatterns = [
    path('tecnologias/', tecnologia_view.TecnologiaList.as_view(), name='tecnologia_list'),
    path('tecnologias/<int:id>', tecnologia_view.TecnolgiaDetalhes.as_view(), name='tecnologia_detalhes'),
    path('vagas/', vaga_view.VagaList.as_view(), name='vaga_list'),
    path('vagas/<int:id>', vaga_view.VagaDetalhes.as_view(), name='vaga_detalhes'),
]
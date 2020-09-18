from django.urls import path, include
from rest_framework.response import Response
from rest_framework.views import APIView

from .views import tecnologia_view, vaga_view, usuario_view
from rest_framework import routers

router = routers.DefaultRouter()


class DocsView(APIView):
    """
    Documentação da API RESTFul
    """

    def get(self, request, *args, **kwargs):
        apidocs = {'tecnologias': request.build_absolute_uri('tecnologias/'),
                   'vagas': request.build_absolute_uri('vagas/'),
                   'usuarios': request.build_absolute_uri('usuarios/')}
        return Response(apidocs)


router.register('tecnologias/', tecnologia_view.TecnologiaList, basename='tecnologias')
router.register('vagas/', vaga_view.VagaList, basename='vagas')
router.register('usuarios/', usuario_view.UsuarioList, basename='usuarios')

urlpatterns = [
    path('', DocsView.as_view()),
    path('', include(router.urls)),
    path('tecnologias/', tecnologia_view.TecnologiaList.as_view(), name='tecnologias'),
    path('tecnologias/<int:id>', tecnologia_view.TecnolgiaDetalhes.as_view(), name='tecnologia_detalhes'),
    path('vagas/', vaga_view.VagaList.as_view(), name='vaga_list'),
    path('vagas/<int:id>', vaga_view.VagaDetalhes.as_view(), name='vaga_detalhes'),
    path('usuarios/', usuario_view.UsuarioList.as_view(), name='usuario_list'),
]

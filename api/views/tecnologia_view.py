from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework import status
from ..entidades import tecnologia
from ..models import Tecnologia
from ..pagination import PaginacaoCustomizada
from ..services import tecnologia_services
from ..serializers import tecnologia_serializer



class TecnologiaList(GenericAPIView):
    # permission_classes = [AllowAny]
    # renderer_classes = [JSONRenderer]
    serializer_class = tecnologia_serializer.TecnologiaSerializer
    queryset = Tecnologia.objects.all()

    def get(self, request, format=None):
        """ Listar tecnologias"""
        paginacao = PaginacaoCustomizada()
        tecnologias = tecnologia_services.listar_tecnologias()
        resultado = paginacao.paginate_queryset(tecnologias, request)
        # serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        # return Response(serializer.data, status=status.HTTP_200_OK)
        serilizer = tecnologia_serializer.TecnologiaSerializer(resultado, context={'request': request}, many=True)
        return paginacao.get_paginated_response(serilizer.data)

    def post(self, request, format=None):
        """ Cadastrar tecnologia"""
        serializer = tecnologia_serializer.TecnologiaSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_bd = tecnologia_services.cadastrar_tecnologia(tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def get_extra_actions(cls):
        return []


class TecnolgiaDetalhes(GenericAPIView):
    # permission_classes = [AllowAny]
    # renderer_classes = [JSONRenderer]
    serializer_class = tecnologia_serializer.TecnologiaSerializer
    queryset = Tecnologia.objects.all()

    def get(self, request, id, format=None):
        """ Trazer dados de tecnologia por id"""

        tecnologia = tecnologia_services.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        """ Editar dados de tecnologia por id"""
        tecnologia_antiga = tecnologia_services.listar_tecnologia_id(id)
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologia_antiga, data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data['nome']
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_services.editar_tecnologia(tecnologia_antiga, tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id, format=None):
        """ Deletar tecnologia por id"""
        tecnologia = tecnologia_services.listar_tecnologia_id(id)
        tecnologia_services.remover_tecnologia(tecnologia)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @classmethod
    def get_extra_actions(cls):
        return []

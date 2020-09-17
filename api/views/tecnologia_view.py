from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from ..entidades import tecnologia
from ..services import tecnologia_services
from ..serializers import tecnologia_serializer
from rest_framework import status


class TecnologiaList(GenericAPIView):
    permission_classes = [AllowAny]

    serializer_class = tecnologia_serializer.TecnologiaSerializer

    def get(self, request, format=None):
        """ Listar tecnologias"""
        tecnologias = tecnologia_services.listar_tecnologias()
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """ Cadastrar tecnologia"""
        serializer = tecnologia_serializer.TecnologiaSerializer(data=request.data)
        if serializer.is_valid():
            nome = serializer.validated_data["nome"]
            tecnologia_nova = tecnologia.Tecnologia(nome=nome)
            tecnologia_bd = tecnologia_services.cadastrar_tecnologia(tecnologia_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TecnolgiaDetalhes(GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = tecnologia_serializer.TecnologiaSerializer

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
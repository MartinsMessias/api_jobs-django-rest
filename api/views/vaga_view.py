from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

from ..entidades import vaga
from ..models import Vaga
from ..serializers import vaga_serializer
from ..services import vaga_service
from ..pagination import PaginacaoCustomizada


class VagaList(GenericAPIView):
    # permission_classes = [AllowAny]
    # renderer_classes = [JSONRenderer]
    serializer_class = vaga_serializer.VagaSerializer
    queryset = Vaga.objects.all()

    def get(self, request, format=None):
        """ Listar vagas"""
        # paginacao = LimitOffsetPagination()
        paginacao = PaginacaoCustomizada()
        vagas = vaga_service.listar_vagas()
        resultado = paginacao.paginate_queryset(vagas, request)
        serilizer = vaga_serializer.VagaSerializer(resultado, context={'request': request}, many=True)
        # serilizer = vaga_serializer.VagaSerializer(vagas, many=True)
        return paginacao.get_paginated_response(serilizer.data)
        # return Response(serilizer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        """ Cadastrar vaga"""
        serializer = vaga_serializer.VagaSerializer(data=request.data)

        if serializer.is_valid():
            titulo = serializer.validated_data['titulo']
            descricao = serializer.validated_data['descricao']
            salario = serializer.validated_data['salario']
            tipo_contratacao = serializer.validated_data['tipo_contratacao']
            local = serializer.validated_data['local']
            quantidade = serializer.validated_data['quantidade']
            contato = serializer.validated_data['contato']
            tecnologias = serializer.validated_data['tecnologias']
            vaga_nova = vaga.Vaga(titulo=titulo, descricao=descricao, salario=salario,
                                  tipo_contratacao=tipo_contratacao,
                                  local=local, quantidade=quantidade, contato=contato, tecnologias=tecnologias)
            vaga_service.cadastrar_vaga(vaga_nova)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @classmethod
    def get_extra_actions(cls):
        return []


class VagaDetalhes(GenericAPIView):
    # permission_classes = [AllowAny]
    queryset = Vaga.objects.all()
    serializer_class = vaga_serializer.VagaSerializer

    def get(self, requisicao, id, format=None, ):
        """Detalhar vaga pelo id"""
        vaga = vaga_service.listar_vaga_id(id)
        serializer = vaga_serializer.VagaSerializer(vaga)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, id, format=None):
        """Editar vaga pelo id"""
        vaga_antiga = vaga_service.listar_vaga_id(id)
        serializer = vaga_serializer.VagaSerializer(vaga_antiga, data=request.data)
        if serializer.is_valid():
            titulo = serializer.validated_data['titulo']
            descricao = serializer.validated_data['descricao']
            salario = serializer.validated_data['salario']
            tipo_contratacao = serializer.validated_data['tipo_contratacao']
            local = serializer.validated_data['local']
            quantidade = serializer.validated_data['quantidade']
            contato = serializer.validated_data['contato']
            tecnologias = serializer.validated_data['tecnologias']
            vaga_nova = vaga.Vaga(titulo=titulo, descricao=descricao, salario=salario,
                                  tipo_contratacao=tipo_contratacao,
                                  local=local, quantidade=quantidade, contato=contato, tecnologias=tecnologias)
            vaga_service.editar_vaga(vaga_antiga, vaga_nova)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, stutus=status.HTTP_400_BAD_REQUEST1)

    def delete(self, request, id, format=None):
        """ Deletar vaga pelo id"""
        vaga = vaga_service.listar_vaga_id(id)
        vaga_service.remover_vaga(vaga)
        return Response(status=status.HTTP_204_NO_CONTENT)

    @classmethod
    def get_extra_actions(cls):
        return []

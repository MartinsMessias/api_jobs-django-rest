from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from ..serializers import vaga_serializer
from ..services import vaga_service

class VagaList(APIView):
    def get(self, request, format=None):
        vagas = vaga_service.listar_vagas()
        serilizer = vaga_serializer.VagaSerializer(vagas, many=True)
        return Response(serilizer.data, status=status.HTTP_200_OK)

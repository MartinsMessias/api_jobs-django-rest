from rest_framework.response import Response
from rest_framework.views import APIView
from ..services import tecnologia_services
from ..serializers import tecnologia_serializer
from rest_framework import status


class TecnologiaList(APIView):
    def get(self, request, format=None):
        tecnologias = tecnologia_services.listar_tecnologias()
        serializer = tecnologia_serializer.TecnologiaSerializer(tecnologias, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

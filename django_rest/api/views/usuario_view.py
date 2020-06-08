from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from ..serializers import usuario_serializer


class UsuarioList(APIView):
    def post(self, request, format=None):
        serializer = usuario_serializer.UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

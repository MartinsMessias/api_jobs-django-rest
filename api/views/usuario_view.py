from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from ..serializers import usuario_serializer


class UsuarioList(GenericAPIView):
    """
    Cadastro de usuários
    """
    permission_classes = [AllowAny]
    serializer_class = usuario_serializer.UsuarioSerializer

    def post(self, request, format=None):
        serializer = usuario_serializer.UsuarioSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

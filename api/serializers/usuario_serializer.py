from django.contrib.auth.models import User
from rest_framework import serializers


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password')

    def create(self, validated_data):
        user = super(UsuarioSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user
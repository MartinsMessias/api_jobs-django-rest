from rest_framework.reverse import reverse
from rest_framework import serializers
from ..models import Vaga


class VagaSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()

    class Meta:
        model = Vaga
        fields = ('id', 'titulo', 'descricao', 'salario', 'local',
                  'quantidade', 'contato', 'tipo_contratacao', 'tecnologias', 'links')

    def get_links(self, obj):
        try:
            request = self.context['request']
            return {
                'self': reverse('vaga_detalhes', kwargs={'id': obj.pk}, request=request),
                'delete': reverse('vaga_detalhes', kwargs={'id': obj.pk}, request=request),
                'update': reverse('vaga_detalhes', kwargs={'id': obj.pk}, request=request),
            }
        except:
            pass


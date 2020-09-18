from rest_framework import serializers
from rest_framework.reverse import reverse

from ..models import Tecnologia


class TecnologiaSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField()
    class Meta:
        model = Tecnologia
        fields = ('nome', 'links', )

    def get_links(self, obj):
        try:
            request = self.context['request']
            return {
                'self': reverse('tecnologia_detalhes', kwargs={'id': obj.pk}, request=request),
                'delete': reverse('tecnologia_detalhes', kwargs={'id': obj.pk}, request=request),
                'update': reverse('tecnologia_detalhes', kwargs={'id': obj.pk}, request=request),
            }
        except:
            pass
from django.conf.urls import url
from django.urls import path, include
urlpatterns = [
    path('', include('api.urls')),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

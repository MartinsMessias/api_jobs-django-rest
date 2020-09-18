from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # path('api-auth/', include('rest_framework.urls'))
]





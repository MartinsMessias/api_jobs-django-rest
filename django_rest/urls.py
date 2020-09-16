from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='DevJobs API')

urlpatterns = [
    path('', schema_view)
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('oauth/', include('oauth2_provider.urls', namespace='oauth2_provider')),
]

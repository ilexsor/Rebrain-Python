from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('', include('metrics_collector.urls')),
    path('admin/', admin.site.urls),
    path('api/', include('metrics_collector.urls'))
]

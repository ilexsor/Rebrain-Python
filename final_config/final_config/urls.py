from django.contrib import admin
from django.urls import path, include
from final_config import metrics_collector

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(metrics_collector.urls))
]

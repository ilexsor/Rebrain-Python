from django.urls import path
from . import views
from .views import ClientAddView, ClientViewSet, MetricsAddView, MetricsViewSet


urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', ClientViewSet.as_view()),
    path('clients/add', ClientAddView.as_view()),
    path('metrics/', MetricsViewSet.as_view()),
    path('metrics/add', MetricsAddView.as_view())
]
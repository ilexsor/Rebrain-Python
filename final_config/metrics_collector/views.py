from django.http.response import HttpResponse
from rest_framework import generics
from .serializer import ClientSerializer, MetricsSerializer
from .models import Client, Metrics


def index(request):
    return HttpResponse("Metrics collector")


class ClientViewSet(generics.ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class ClientAddView(generics.CreateAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class MetricsViewSet(generics.ListAPIView):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer


class MetricsAddView(generics.CreateAPIView):
    queryset = Metrics.objects.all()
    serializer_class = MetricsSerializer

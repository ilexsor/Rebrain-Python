from rest_framework import serializers
from .models import Client, Metrics


class ClientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Client
        fields = ['id', 'ip_address', 'description', 'name']


class MetricsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Metrics
        fields = ['id', 'host_info', 'disk_info', 'memory_info', 'cpu_info', 'load_avg']


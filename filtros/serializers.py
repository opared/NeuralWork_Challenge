from rest_framework import serializers
from .models import ArchViajes


class ArchViajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchViajes
        fields = ('file', 'description', 'uploaded_at')


class FiltroSemanaSerializer(serializers.Serializer):
    fecha = serializers.CharField(max_length=10)


class CuadradoSerializer(serializers.Serializer):
    coor_up = serializers.FloatField()
    coor_down = serializers.FloatField()
    coor_right = serializers.FloatField()
    coor_left = serializers.FloatField()
    columna = serializers.CharField(max_length=20)

class FiltroHoraSerializer(serializers.Serializer):
    hora = serializers.CharField(max_length=10)

class FiltroSourceSerializer(serializers.Serializer):
    source = serializers.CharField(max_length=30)

class FiltroRegionSerializer(serializers.Serializer):
    region = serializers.CharField(max_length=30)


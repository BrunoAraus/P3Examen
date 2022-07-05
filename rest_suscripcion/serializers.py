from rest_framework import serializers
from core.models import Suscripciones

class SuscripcionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suscripciones
        fields = ['codigo','usuario','estado']
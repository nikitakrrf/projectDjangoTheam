from rest_framework import serializers
from .models import Themes



class WcapiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Themes
        fields = ('id_themes', 'category', 'amount')
    
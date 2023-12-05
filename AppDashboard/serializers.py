from rest_framework import serializers
from .models import App

class CreateAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'

class UpdateAppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'
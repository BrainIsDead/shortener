from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Link


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ('full_url',)


class LinkListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = '__all__'

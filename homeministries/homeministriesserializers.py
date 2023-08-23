from rest_framework import serializers

from .models import Ministries, HomeMinistries


class MinistriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ministries
        fields = '__all__'


class HomeMinistriesSerializer(serializers.ModelSerializer):
    ministries = MinistriesSerializer(many=True, read_only=True)
    class Meta:
        model = HomeMinistries
        fields = '__all__'


from rest_framework import serializers

from .models import PrayerCity


class PrayerCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerCity
        fields = "__all__"


class PrayerCityShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerCity
        fields = ("alias", "title", "short_description")

from rest_framework import serializers

from .models import PrayerConnect, PrayerConnectCenter, PrayerConnectDirector


class PrayerConnectDirectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerConnectDirector
        fields = "__all__"


class PrayerConnectCenterSerializer(serializers.ModelSerializer):
    directors = PrayerConnectDirectorSerializer(many=True, read_only=True)

    class Meta:
        model = PrayerConnectCenter
        fields = "__all__"


class PrayerConnectSerializer(serializers.ModelSerializer):
    centers = PrayerConnectCenterSerializer(many=True, read_only=True)

    class Meta:
        model = PrayerConnect
        fields = "__all__"


class PrayerConnectShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerConnect
        fields = ("alias", "title", "short_description")

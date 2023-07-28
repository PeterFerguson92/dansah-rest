from rest_framework import serializers

from .models import HomeActivity
from leadershipinstitute.leadershipinstituteserializers import (
    LeadershipInstituteShortSerializer,
)
from prayercity.prayercityserializers import PrayerCityShortSerializer
from powerliving.powerlivingserializers import PowerLivingShortSerializer
from prayerconnect.prayerconnectserializers import PrayerConnectShortSerializer


class HomeActivitySerializer(serializers.ModelSerializer):
    leadership_institute = LeadershipInstituteShortSerializer(read_only=True)
    prayer_city = PrayerCityShortSerializer(read_only=True)
    power_living = PowerLivingShortSerializer(read_only=True)
    prayer_connect = PrayerConnectShortSerializer(read_only=True)

    class Meta:
        model = HomeActivity
        fields = "__all__"

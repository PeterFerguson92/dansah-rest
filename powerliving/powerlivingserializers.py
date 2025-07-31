from rest_framework import serializers

from .models import Article, PowerLiving, MonthlyPowerLiving


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = "__all__"


class MonthlyPowerLivingSerializer(serializers.ModelSerializer):
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = MonthlyPowerLiving
        fields = "__all__"


class PowerLivingSerializer(serializers.ModelSerializer):
    monthly_power_living = MonthlyPowerLivingSerializer(many=True, read_only=True)

    class Meta:
        model = PowerLiving
        fields = "__all__"


class PowerLivingSerializer(serializers.ModelSerializer):
    monthly_power_living = MonthlyPowerLivingSerializer(many=True, read_only=True)

    class Meta:
        model = PowerLiving
        fields = "__all__"


class PowerLivingShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = PowerLiving
        fields = ("alias", "title", "short_description")

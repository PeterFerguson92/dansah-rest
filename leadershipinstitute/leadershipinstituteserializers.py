from rest_framework import serializers

from .models import (
    Assesment,
    Assignment,
    Course,
    Category,
    Material,
    LeadershipInstitute,
    Reading,
    Video,
)


class AssignmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assignment
        fields = "__all__"


class AssesmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assesment
        fields = "__all__"


class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = "__all__"


class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = "__all__"


class MaterialSerializer(serializers.ModelSerializer):
    videos = VideoSerializer(many=True, read_only=True)
    readings = ReadingSerializer(many=True, read_only=True)
    assignments = AssignmentSerializer(many=True, read_only=True)
    assesments = AssesmentSerializer(many=True, read_only=True)

    class Meta:
        model = Material
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class CategoryNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name"]


class CourseSerializer(serializers.ModelSerializer):
    level = CategoryNameSerializer(read_only=True)
    materials = MaterialSerializer(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class LeadershipInstituteSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = LeadershipInstitute
        fields = "__all__"


class LeadershipInstituteShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadershipInstitute
        fields = ("alias", "title", "short_description")

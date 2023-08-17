from rest_framework import status, generics
from rest_framework.response import Response

from .leadershipinstituteserializers import (
    CategorySerializer,
    CourseSerializer,
    LeadershipInstituteSerializer,
    StudentSerializer,
)
from .models import Course, Category, LeadershipInstitute, Student


class StudentView(generics.GenericAPIView):
    serializer_class = StudentSerializer

    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except:
            return None

    def get_student(self, email):
        try:
            return Student.objects.filter(email=email)
        except:
            return None

    def post(self, request):
        if len(request.data) is 0:
            return Response(
                {
                    "status": "fail",
                    "message": f"Student information not available",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        try:
            student = self.get_student(request.data["email"])
            print(student)
            if student:
                return Response(
                    {
                        "status": "fail",
                        "message": f"Student with this email already registered",
                    },
                    status=status.HTTP_401_UNAUTHORIZED,
                )
            course_id = request.data["course_id"]
            course = self.get_course(pk=course_id)
            serializer = StudentSerializer(data=request.data, partial=True)
            if serializer.is_valid():
                result = serializer.save()
                course.students.add(result)
                result.save()
                return Response({"status": "success"}, status=status.HTTP_201_CREATED)
            return Response(
                {
                    "status": "fail",
                    "message": f"Student information not saved",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception:
            return Response(
                {
                    "status": "fail",
                    "message": f"Student information not valid",
                },
                status=status.HTTP_400_BAD_REQUEST,
            )


class CoursesView(generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get(self, request):
        result = Course.objects.all()
        if not result:
            return Response(
                {
                    "status": "fail",
                    "message": f"Leadership institute courses not available",
                },
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(result, many=True)
        return Response({"status": "success", "result": serializer.data})


class CourseDetailView(generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_course(self, pk):
        try:
            return Course.objects.get(pk=pk)
        except:
            return None

    def get(self, request, pk):
        course = self.get_course(pk=pk)
        if course is None:
            return Response(
                {"status": "fail", "message": f"Course with Id: {pk} not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(course)
        return Response({"status": "success", "result": serializer.data})


class CoursesByCategoryView(generics.GenericAPIView):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()

    def get_course_by_category(self, level):
        try:
            return Course.objects.filter(level__name__contains=level)
        except:
            return None

    def get(self, request):
        level = request.query_params.get("level", None)
        print(level)
        courses = self.get_course_by_category(level)
        print(courses)
        if courses is None:
            return Response(
                {
                    "status": "fail",
                    "message": f"Error retrieving courses with level: {level}",
                },
                status=status.HTTP_404_NOT_FOUND,
            )

        serializer = self.serializer_class(courses, many=True)
        return Response({"status": "success", "result": serializer.data})


class CategoryView(generics.GenericAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()

    def get(self, request):
        result = Category.objects.all()
        if not result:
            return Response(
                {"status": "Leadership institute categories not available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(result, many=True)
        return Response({"status": "success", "result": serializer.data})


class LeadershipInstituteView(generics.GenericAPIView):
    serializer_class = LeadershipInstituteSerializer
    queryset = LeadershipInstitute.objects.all()

    def get(self, request):
        result = LeadershipInstitute.objects.all()
        if not result:
            return Response(
                {"status": "Leadership institute not available"},
                status=status.HTTP_404_NOT_FOUND,
            )
        serializer = self.serializer_class(result, many=True)
        return Response({"status": "success", "result": serializer.data})

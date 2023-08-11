from django.urls import path

from .views import (
    CoursesView,
    CourseDetailView,
    CoursesByCategoryView,
    CategoryView,
    LeadershipInstituteView,
    StudentView,
)

urlpatterns = [
    path("", LeadershipInstituteView.as_view()),
    path("categories/", CategoryView.as_view()),
    path("courses/", CoursesView.as_view()),
    path("course/<uuid:pk>", CourseDetailView.as_view()),
    path("courses/category", CoursesByCategoryView.as_view()),
    path("courses/student", StudentView.as_view()),
]

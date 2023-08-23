from django.urls import path

from .views import HomeMinistriesView, MinistryDetailView

urlpatterns = [
    path("", HomeMinistriesView.as_view()),
    path("ministry/<uuid:pk>", MinistryDetailView.as_view()),
]

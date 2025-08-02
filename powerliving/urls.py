from django.urls import path

from .views import ArticleDetailView, PowerLivingView, MonthlyPowerLivingDetailView

urlpatterns = [
    path("", PowerLivingView.as_view()),
    path("<uuid:pk>", MonthlyPowerLivingDetailView.as_view()),
    path("article/<uuid:pk>", ArticleDetailView.as_view()),
]

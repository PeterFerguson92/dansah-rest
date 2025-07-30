from django.urls import path

from .views import PowerLivingView, MonthlyPowerLivingDetailView

urlpatterns = [
    path("", PowerLivingView.as_view()),
    path("<uuid:pk>", MonthlyPowerLivingDetailView.as_view()),
]

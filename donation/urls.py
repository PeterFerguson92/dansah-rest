from django.urls import path

from .views import DonationView

urlpatterns = [
    path("", DonationView.as_view()),
]

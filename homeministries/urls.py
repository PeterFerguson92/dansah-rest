from django.urls import path

from .views import HomeMinistriesView

urlpatterns = [
    path("", HomeMinistriesView.as_view()),
]

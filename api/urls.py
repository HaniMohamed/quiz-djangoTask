from django.urls import path

from .views import AnswerAPIView

urlpatterns = [
    path('', AnswerAPIView.as_view()),
]

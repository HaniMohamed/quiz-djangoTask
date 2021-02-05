from django.urls import path

from .views import AnswerGroupedDate

urlpatterns = [
    path('', AnswerGroupedDate.as_view()),
]

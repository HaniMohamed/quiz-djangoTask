from django.shortcuts import render
from rest_framework import generics

from quiz.models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer

# Create your views here.


class AnswerAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionAPIView(generics.ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

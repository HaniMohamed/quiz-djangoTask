from rest_framework import generics
from .permissions import IsAdminNotSuperuser

from quiz.models import Answer, Question
from .serializers import AnswerSerializer, QuestionSerializer


# Create your views here.

class AnswerAPIView(generics.ListAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer


class QuestionAPIView(generics.ListAPIView):
    permission_classes = [IsAdminNotSuperuser]
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

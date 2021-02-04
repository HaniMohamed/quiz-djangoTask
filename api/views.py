from rest_framework import generics

from quiz.models import Answer
from .permissions import IsAdminNotSuperuser
from .serializers import AnswerQuizSerializer


# Create your views here.

class AnswerAPIView(generics.ListAPIView):
    permission_classes = [IsAdminNotSuperuser]
    queryset = Answer.objects.all()
    serializer_class = AnswerQuizSerializer

    def get_queryset(self):
        queryset = Answer.objects.all()
        from_date = self.request.query_params.get('from_date', None)
        to_date = self.request.query_params.get('to_date', None)
        if from_date:
            return queryset.filter(created__range=[from_date, to_date])
        else:
            return Answer.objects.all()

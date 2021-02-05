from rest_framework import generics

from quiz.models import Answer
from .permissions import IsAdminNotSuperuser
from .serializers import AnswerQuizSerializer, AnswerLogSerializer


# Create your views here.


class AnswerGroupedDate(generics.ListAPIView):
    permission_classes = [IsAdminNotSuperuser]
    serializer_class = AnswerLogSerializer

    def get_queryset(self):
        queryset = Answer.objects.order_by('-created').distinct('created').only('created')
        from_date = self.request.query_params.get('from_date', None)
        to_date = self.request.query_params.get('to_date', None)
        if from_date:
            return queryset.filter(created__range=[from_date, to_date])
        else:
            return queryset

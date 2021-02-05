from rest_framework import serializers

from quiz.models import Answer, Question


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('id', 'choice',)
        depth = 1


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True, )
    answers_count = serializers.IntegerField(
        source='answers.count',
        read_only=True
    )

    class Meta:
        model = Question
        fields = ('text', 'answers_count', 'answers',)


class AnswerQuizSerializer(serializers.ModelSerializer):
    question = QuestionSerializer()

    class Meta:
        model = Answer
        fields = ('question', )


class AnswerLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['created', 'questions_count', 'answers', ]

    answers = serializers.SerializerMethodField('get_answer')
    questions_count = serializers.SerializerMethodField()



    @staticmethod
    def get_answer(obj):
        answers = Answer.objects.filter(created=obj.created)
        answer_serializer = AnswerQuizSerializer(answers, many=True)
        return answer_serializer.data,



    def get_questions_count(self, obj):
        return Answer.objects.filter(created=obj.created).count()

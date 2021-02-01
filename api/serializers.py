from rest_framework import serializers
from quiz.models import Answer, Question, Choice


class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ('id', 'text',)


class AnswerSerializer(serializers.ModelSerializer):
    choice = ChoiceSerializer()

    class Meta:
        model = Answer
        fields = ('created', 'id', 'choice')


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)
    answers_count = serializers.IntegerField(
        source='answers.count',
        read_only=True
    )

    class Meta:
        model = Question
        fields = ('text', 'answers_count', 'answers',)

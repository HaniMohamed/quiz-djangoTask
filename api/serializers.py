from datetime import datetime

from rest_framework import serializers

from quiz.models import Answer, Question, Choice


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
    # questions_count = serializers.IntegerField(
    #     source='questions.count',
    #     read_only=True
    # )

    class Meta:
        model = Answer
        fields = ('created','question',)


from .models import *
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.serializers import ModelSerializer

from .models import Test, Question, Answer, TestAttempt

class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ['question','id', 'text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, read_only=True)

    class Meta:
        model = Question
        fields = ['test','id', 'text', 'order', 'answers']

class TestSerializer(serializers.ModelSerializer):
    questions = QuestionSerializer(many=True, read_only=True)

    class Meta:
        model = Test
        fields = ['id', 'title', 'description', 'time_limit', 'created_by', 'created_at', 'updated_at', 'questions']


class AttemptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attempt
        fields = ['testAttempt','id', 'question','answer']
        read_only_fields = []
  
class TestAttemptSerializer(serializers.ModelSerializer):
    attempts = AttemptSerializer(many=True,read_only=True)
    class Meta:
        model = TestAttempt
        fields = ['id', 'test','attempts','user', 'start_time', 'end_time', 'score']
        read_only_fields = ['start_time', 'score']
      

    
  
class BadgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Badge
        fields = ['id', 'test', 'user', 'description', 'created_at']
        read_only_fields = ['created_at']
# tests/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Test, TestAttempt, Question,Answer
from .serializers import AnswerSerializer, TestSerializer, TestAttemptSerializer,QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    
    
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    

    
class TestViewSet(viewsets.ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['post'])
    def start_test(self, request, pk=None):
        test = self.get_object()
        user = request.user
        
        # Check if there's an ongoing attempt
        ongoing_attempt = TestAttempt.objects.filter(test=test, user=user, end_time__isnull=True).first()
        if ongoing_attempt:
            return Response({"error": "You have an ongoing attempt for this test."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new test attempt
        attempt = TestAttempt.objects.create(test=test, user=user)
        return Response(TestAttemptSerializer(attempt).data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def submit_test(self, request, pk=None):
        test = self.get_object()
        user = request.user
        
        attempt = TestAttempt.objects.filter(test=test, user=user, end_time__isnull=True).first()
        if not attempt:
            return Response({"error": "No ongoing test attempt found."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Calculate score (implement your scoring logic here)
        score = self.calculate_score(attempt, request.data.get('answers', {}))
        
        attempt.end_time = timezone.now()
        attempt.score = score
        attempt.save()
        
        return Response(TestAttemptSerializer(attempt).data)

    def calculate_score(self, attempt, submitted_answers):
        # Implement your scoring logic here
        # This is a simplified example
        correct_answers = 0
        total_questions = attempt.test.questions.count()
        
        for question_id, answer_id in submitted_answers.items():
            question = attempt.test.questions.get(id=question_id)
            if question.answers.filter(id=answer_id, is_correct=True).exists():
                correct_answers += 1
        
        return (correct_answers / total_questions) * 100 if total_questions > 0 else 0
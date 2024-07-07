# tests/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Test,Attempt, TestAttempt,Badge, Question,Answer
from .serializers import AttemptSerializer,AnswerSerializer,BadgeSerializer, TestSerializer, TestAttemptSerializer,QuestionSerializer

class AnswerViewSet(viewsets.ModelViewSet):
    model = Answer
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        if request.user.is_superuser:
            objects = self.model.objects.all()
            
            objects.delete()
       
        
        return Response(status=status.HTTP_200_OK)
    
    
class QuestionViewSet(viewsets.ModelViewSet):
    model = Question
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        if request.user.is_superuser:
            objects = self.model.objects.all()
            objects.delete()
       
        
        return Response(status=status.HTTP_200_OK)
    
    
class TestViewSet(viewsets.ModelViewSet):
    model = Test
    queryset = Test.objects.all()
    serializer_class = TestSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        if request.user.is_superuser:
            objects = self.model.objects.all()
            
            objects.delete()
       
        
        return Response(status=status.HTTP_200_OK)
    
    @action(detail=True, methods=['get'])
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

    @action(detail=True, methods=['get'])
    def submit_test(self, request, pk=None):
        test = self.get_object()
        user = request.user
        
        test_attempt = TestAttempt.objects.filter(test=test, user=user, end_time__isnull=True).first()
        if not test_attempt:
            return Response({"error": "No ongoing test attempt found."}, status=status.HTTP_400_BAD_REQUEST)
        
        # Calculate score (implement your scoring logic here)
        score = self.calculate_score(test_attempt)
        
        test_attempt.end_time = timezone.now()
        
        if(score >= 50):
            Badge.objects.create(user,test,description="Congratulations you did it !!")
        test_attempt.score = score
        test_attempt.save()
        
        return Response(TestAttemptSerializer(test_attempt).data)

    def calculate_score(self, test_attempt):
        # Implement your scoring logic here
        # This is a simplified example
        correct_answers = 0
        total_questions = test_attempt.test.questions.count()
        print(total_questions)
        for attempt in test_attempt.attempts.all():
            question = attempt.question.answers.filter(is_correct=True).first()
            answer = attempt.answer
            
            if question.id == answer.id:
                correct_answers += 1
        
        return (correct_answers / total_questions) * 100 if total_questions > 0 else 0
    
    
class TestAttemptViewSet(viewsets.ModelViewSet):
    model = TestAttempt
    queryset = TestAttempt.objects.all()
    serializer_class = TestAttemptSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        if request.user.is_superuser:
            objects = self.model.objects.all()
            
            objects.delete()
       
        
        return Response(status=status.HTTP_200_OK)
    
    
class BadgeViewSet(viewsets.ModelViewSet):
    model = Badge
    queryset = Badge.objects.all()
    serializer_class = BadgeSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        if request.user.is_superuser:
            objects = self.model.objects.all()
            
            objects.delete()
       
        
        return Response(status=status.HTTP_200_OK)
   

class AttemptViewSet(viewsets.ModelViewSet):
    model = Attempt
    queryset = Attempt.objects.all()
    serializer_class = AttemptSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        if request.user.is_superuser:
            objects = self.model.objects.all()
            
            objects.delete()
       
        
        return Response(status=status.HTTP_200_OK)
     

class TestAttemptViewSet(viewsets.ModelViewSet):
    model = TestAttempt
    queryset = TestAttempt.objects.all()
    serializer_class = TestAttemptSerializer
    permission_classes = [IsAuthenticated]
    
    @action(detail=False, methods=['get'])
    def deleteAll(self, request):
        
        if request.user.is_superuser:
            objects = self.model.objects.all()
            
            objects.delete()
       
        
        return Response(status=status.HTTP_200_OK)
     

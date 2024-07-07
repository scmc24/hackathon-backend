from django.db import models
from accounts.models import User
# Create your models here.

class Test(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    time_limit = models.IntegerField(help_text="Time limit in minutes")
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Question(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    text = models.TextField()
    order = models.IntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.test.title} - Question {self.order}"


class Answer(models.Model):
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    text = models.CharField(max_length=200)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.question.text[:20]}... - {self.text[:20]}..."


class TestAttempt(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    score = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.test.title}"

class Attempt(models.Model):
    testAttempt = models.ForeignKey(TestAttempt, on_delete=models.CASCADE,related_name='attempts')
    question = models.ForeignKey(Question,on_delete=models.SET_NULL,null=True)
    answer = models.ForeignKey(Answer,on_delete=models.SET_NULL,null=True )
    

class Badge(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    test = models.ForeignKey(Test, on_delete=models.SET_NULL,null=True)
    description = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now=True)
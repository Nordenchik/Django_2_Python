from django.db import models

class Quiz(models.Model):
    quiz_id = models.BigAutoField(primary_key = True)
    title = models.TextField()
    description = models.TextField()

    def __str__(self): return self.title

class Question(models.Model):
    question_id = models.BigAutoField(primary_key = True)
    quiz = models.ForeignKey(Quiz, related_name = 'questions', on_delete = models.CASCADE)
    content = models.TextField()

    def __str__(self): return self.content

class Option(models.Model):
    option_id = models.BigAutoField(primary_key = True)
    question = models.ForeignKey(Question, related_name = 'options', on_delete = models.CASCADE)
    content = models.TextField()
    is_correct = models.BooleanField()

    def __str__(self): return self.content

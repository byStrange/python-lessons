from django.db import models

# Create your models here.

class Quiz(models.Model):
    question = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    options = models.CharField(max_length=200)

    def __str__(self):
        return self.answer

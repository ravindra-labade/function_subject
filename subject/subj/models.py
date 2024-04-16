from django.db import models


class Subject(models.Model):
    subject_name = models.CharField(max_length=10)
    total_contents = models.IntegerField()
    total_poems = models.IntegerField()
    subject_teacher = models.CharField(max_length=20)
    choice = [('home', 'Home'), ('class', 'Class')]
    study_mode = models.CharField(max_length=10, choices=choice)


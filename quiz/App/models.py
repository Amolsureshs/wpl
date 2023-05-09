from django.db import models

# Create your models here.
class Ques(models.Model):
    Question=models.CharField(max_length=255)
    op1=models.CharField(max_length=255)
    op2=models.CharField(max_length=255)
    op3=models.CharField(max_length=255)
    op4=models.CharField(max_length=255)
    ans=models.CharField(max_length=255)
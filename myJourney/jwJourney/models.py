from django.db import models


# Create your models here.
class LearningMyJourney(models.Model):
    title = models.CharField(max_length=300)
    descrpition = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
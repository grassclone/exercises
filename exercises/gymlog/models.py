from django.db import models
from django.utils import timezone

# Create your models here.

class Exercise(models.Model):
	exercise_name = models.CharField(max_length=20)
	date_completed = models.DateTimeField(default=timezone.now)
	reps = models.IntegerField(default=1)

	def __str__ (self):
		return self.exercise_name
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

class Classroom(models.Model):
	name = models.CharField(max_length=120)
	teacher =  models.ForeignKey(User,default=1, on_delete=models.CASCADE)
	subject = models.CharField(max_length=120)
	year = models.IntegerField()

	def get_absolute_url(self):
		return reverse('classroom-detail', kwargs={'classroom_id':self.id})


class Student(models.Model):
	name = models.CharField(max_length=120)
	date_of_birth = models.DateTimeField()

	GENDER_CHOICES = (
        ('GENDER', 'Gender'),
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
    )
	gender = models.CharField(
        max_length=6,
        choices=GENDER_CHOICES,
        default='GENDER',
    )
	exam_grade = models.FloatField()
	classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')

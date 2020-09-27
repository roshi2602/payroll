from django.db import models

# Create your models here.
class Employee(models.Model):
	first_name=models.CharField(max_length=200)
	last_name=models.CharField(max_length=200)
	id_number=models.IntegerField()
	phone_number=models.IntegerField()
	job_title=models.CharField(max_length=200)
	department=models.CharField(max_length=200)
	email=models.EmailField()
	start_date=models.DateTimeField()
	end_date=models.DateTimeField()
	location=models.CharField(max_length=200)


	def __str__(self):
		return f"{ self.first_name}, {self.last_name}"
from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from emp.models import Employee
# Create your models here

class Payroll(models.Model):
	STATUS_CHOICES=(
		('C', 'cash'),
		('D', 'digital'),

		)
	salary=models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(40000)])
	overtime_pay=models.FloatField()
	tax= models.FloatField()
	gross_pay=models.FloatField()
	net_pay=models.FloatField()
	deduction=models.FloatField()
	payment_method=models.CharField(max_length=200, choices=STATUS_CHOICES)
	employee=models.ForeignKey(Employee,on_delete=models.CASCADE)



	class Meta:
		verbose_name="Employee Payroll"
		ordering = ("salary","overtime_pay","tax","gross_pay","net_pay","deduction","employee")
	
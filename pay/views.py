from django.shortcuts import render
from pay.models import Payroll
from django.views.generic import View
from emp.models import Employee
from pay.admin import PayrollAdminForm
from django.http import HttpResponse
# Create your views here.
class PayrollView(View):
	model=Payroll
	form_class=PayrollAdminForm
	fields=['salary','overtime_pay','tax','gross_pay','net_pay','deduction','payment_method','employee']
	template_name='pay/payroll.html'
	context_object_name="payrolls"

		


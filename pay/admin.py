from django.contrib import admin
from pay.models import Payroll,Employee
from django.urls import reverse
from django.utils.http import urlencode
from django import forms

class PayrollAdminForm(forms.ModelForm): #to change forms
	class Meta:
		model=Payroll
		fields="__all__"

		def clean_first_name(self):
			if self.clean_data['gross_pay'] =="20000":
				raise forms.ValidationError("NOT VALID")
			return self.clean_data['gross_pay']





@admin.register(Payroll)
class PayrollAdmin(admin.ModelAdmin):
	form=PayrollAdminForm
	list_display=('employee','net_pay','tax','gross_pay',"overtime_pay","deduction",'salary',"show_count")
	list_filter=("employee",)
	search_fields=("salary",)
	fields=('employee','salary','gross_pay','net_pay','tax','overtime_pay','deduction')


	def get_form(self,request, ob=None,**kwargs): #to change forms
		form=super().get_form(request, ob,**kwargs)
		form.base_fields["salary"].label="ALL SALARIES"
		return form


	def show_count(self,obj):  #tochange lists
		from django.db.models import Count
		result=Payroll.objects.all().aggregate(Count('salary'))
		return result["salary__count"]

	show_count.short_description =" Count salary"




@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	list_display=('first_name','last_name','department','view_employees')

	def view_employees(self,obj):
		from django.utils.html import format_html
		count=obj.payroll_set.count()
		url=(
			reverse("admin:pay_payroll_changelist")
			+ "?"
			+ urlencode({"employee__id":f"{obj.id}"})

		)
		return format_html('<a href="{}">{}employees</a>',url, count)
		view_employees.short_description="employees"

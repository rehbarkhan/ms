from django.contrib import admin
from finance.models import FinanceDepartment,FinanceSalary
# Register your models here.

admin.site.register(FinanceSalary)

admin.site.register(FinanceDepartment)
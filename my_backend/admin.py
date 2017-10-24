from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(company)
admin.site.register(company_offer)
admin.site.register(student)
admin.site.register(applicant_detail)
from django.db import models

# Create your models here.
class applicant_detail(models.Model):
	userid = models.CharField(max_length=100)
	name = models.CharField(max_length=100)	

	def __str__(self):
		return self.name


class company_offer(models.Model):

	offer_type = models.CharField(max_length=100)
	industry = models.CharField(max_length=100)
	job_description = models.CharField(max_length=1000)
	requirements = models.CharField(max_length=1000)
	role = models.CharField(max_length=100)
	salary = models.CharField(max_length=100)
	recruitment_procedure = models.CharField(max_length=100)
	allowed_branches = models.CharField(max_length=100)
	company_id = models.CharField(max_length=100)
	interested_students=models.CharField(max_length=1000, blank=True)
	shortlisted_students=models.CharField(max_length=1000,blank=True)
	def __str__(self):
		return self.company_id

class student(models.Model):
	class meta:
		verbose_name_plural = "students"

	userid = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=100)
	offers =  models.ManyToManyField(company_offer,blank=True)
	department = models.CharField(max_length=100)
	program = models.CharField(max_length=100)
	
	photo = models.ImageField(upload_to='media/students/images',blank=True, null=True)
	resume=models.FileField(upload_to='media/students/resume',blank=True, null=True)
	
	def __str__(self):
		return self.name	




class company(models.Model):
	class meta:
		verbose_name_plural = "companies"

	userid = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	#offers = models.ManyToManyField(company_offer,blank=True)
	logo = models.ImageField(upload_to='media/company',blank=True, null=True)
	website =models.CharField(max_length=100)
	location = models.CharField(max_length=100)
	contact = models.CharField(max_length=100)
	def __str__(self):
		return self.name


class query(models.Model):
	class meta:
		verbose_name_plural="queries"
	userid=models.CharField(max_length=100)
	description=models.CharField(max_length=1000)
	datetime=models.CharField(max_length=1000)
	
	def __str__(self):
		return self.userid	






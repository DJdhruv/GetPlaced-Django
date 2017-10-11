from django.db import models

# Create your models here.



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

	def __str__(self):
		return self.company_id


class company(models.Model):
	class meta:
		verbose_name_pural = 'companies'

	userid = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	offers = models.ManyToManyField(company_offer)

	def __str__(self):
		return self.name

class student(models.Model):
	class meta:
		verbose_name_pural = 'students'

	userid = models.CharField(max_length=100)
	password = models.CharField(max_length=100)
	name = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	contact_number = models.CharField(max_length=100)
	offers =  models.ManyToManyField(company_offer)
	
	def __str__(self):
		return self.name	





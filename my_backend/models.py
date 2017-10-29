from django.db import models

# Create your models here.


## Model for offers
#  This model stores list of all offers added by companies
#
# These offers are shown in the "Offers" Tab in student interface
class company_offer(models.Model):
	## Type of offer
	offer_type = models.CharField(max_length=100)
	## Broad Area of offer
	industry = models.CharField(max_length=100)
	## Detailed decription of offer
	job_description = models.CharField(max_length=1000)
	## Requirements of offer
	requirements = models.CharField(max_length=1000)
	## Role of the selected student
	role = models.CharField(max_length=100)
	## Salary/Stipend provided
	salary = models.CharField(max_length=100)
	## Procedure of recruiting students
	recruitment_procedure = models.CharField(max_length=100)
	## Students of which branches are allowed to apply for the offer
	allowed_branches = models.CharField(max_length=100)
	## ID of company
	company_id = models.CharField(max_length=100)
	## Comma separated string of user id's of interested students
	interested_students=models.CharField(max_length=1000, blank=True)
	## Comma separated string of user id's of shortlisted students
	shortlisted_students=models.CharField(max_length=1000,blank=True)
	## The displayed name of each object
	def __str__(self):
		return self.company_id

## Model for students
#  This model stores list of all students

class student(models.Model):
	## The default class within a model
	class meta:
		## Defining plural name of model
		verbose_name_plural = "students" 
	## userid of student
	userid = models.CharField(max_length=100)
	## password of student
	password = models.CharField(max_length=100)
	## name of student
	name = models.CharField(max_length=100)
	## email id of student
	email = models.CharField(max_length=100)
	## contact number of student
	contact_number = models.CharField(max_length=100)
	#offers =  models.ManyToManyField(company_offer,blank=True)
	## department of student
	department = models.CharField(max_length=100)
	## program of student
	program = models.CharField(max_length=100)
	## profile picture of student
	photo = models.ImageField(upload_to='media/students/images',blank=True, null=True)
	## resume of student
	resume=models.FileField(upload_to='media/students/resume',blank=True, null=True)
	## The displayed name of each object
	def __str__(self):
		return self.name	



## Model for companies
#  This model stores list of all companies

class company(models.Model):
	## The default class within a model
	class meta:
		## Defining plural name of model
		verbose_name_plural = "companies"
	## userid of company
	userid = models.CharField(max_length=100)
	## password of company
	password = models.CharField(max_length=100)
	## name of company
	name = models.CharField(max_length=100)
	#offers = models.ManyToManyField(company_offer,blank=True)
	## logo of company
	logo = models.ImageField(upload_to='media/company',blank=True, null=True)
	## website of company
	website =models.CharField(max_length=100)
	## location of company headquarters
	location = models.CharField(max_length=100)
	## contact number for company
	contact = models.CharField(max_length=100)
	## The displayed name of each object
	def __str__(self):
		return self.name

## Model for query
#  This model stores list of all queries
#
# This is shown in "query" tab in student interface
class query(models.Model):
	## The default class within a model
	class meta:
		## Defining plural name of model
		verbose_name_plural="queries"
	## userid of student posting the query
	userid=models.CharField(max_length=100)
	## description of the query
	description=models.CharField(max_length=1000)
	## time when the query is posted
	datetime=models.CharField(max_length=1000)
	## The displayed name of each object
	def __str__(self):
		return self.userid	






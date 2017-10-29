from rest_framework import serializers
from .models import *


## Serializer for Offers
# This will parse the offer-data array and convert it into JSON format which can be accessed by "GET" request.
class OffersSerializer(serializers.ModelSerializer):
	
	## It is a predefined class of a serializer
	class Meta:
		## Defines a models for serializer to parse accordingly.
		model = company_offer
		## Defines the fields which have to be parsed
		fields = '__all__'

## Serializer for CompanyLogin
# This will parse the company-login-data array and convert it into JSON format which can be accessed by "GET" request.
class CompanyLoginSerializer(serializers.ModelSerializer):

	## It is a predefined class of a serializer	
	class Meta:
		## Defines a models for serializer to parse accordingly.
		model = company
		## Defines the fields which have to be parsed
		fields = ('userid', 'password')

## Serializer for Company
# This will parse the company-data array and convert it into JSON format which can be accessed by "GET" request.
class CompanySerializer(serializers.ModelSerializer):
	#offers = OffersSerializer(read_only=True, many=True)
	## It is a predefined class of a serializer
	class Meta:
		## Defines a models for serializer to parse accordingly.
		model = company
		## Defines the fields which have to be parsed
		fields = '__all__'

## Serializer for Students
# This will parse the student-data array and convert it into JSON format which can be accessed by "GET" request.
class StudentSerializer(serializers.ModelSerializer):
	#offers = OffersSerializer(read_only=True, many=True)
	## It is a predefined class of a serializer
	class Meta:
		## Defines a models for serializer to parse accordingly.
		model = student
		## Defines the fields which have to be parsed
		fields = '__all__'

## Serializer for Queries
# This will parse the query-data array and convert it into JSON format which can be accessed by "GET" request.
class QuerySerializer(serializers.ModelSerializer):
	## It is a predefined class of a serializer
	class Meta:
		## Defines a models for serializer to parse accordingly.
		model=query
		## Defines the fields which have to be parsed
		fields='__all__'		

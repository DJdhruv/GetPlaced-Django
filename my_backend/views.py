from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.views import APIView
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
# Create your views here.

## Viewset for offers
# This will automatically generate a webpage interface along with predefined methods.
# These mehods will allow us to "GET", "PUT", "PATCH" and "DELETE" data.
class OffersViewSet(viewsets.ModelViewSet):

	## Define list of Offers to be shown.
	queryset = company_offer.objects.all()
	## Define serializer for the Viewset
	serializer_class = OffersSerializer

	## Override the "GET" method
	def get(self, request, format=None):
		users = company_offer.objects.all()
		serializer = OffersSerializer(users, many=True)
		return Response(serializer.data)
	## Override the "PUT" method
	def put(self, request, format=None):
		serializer = OffersSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	## Override the "DELETE" method
	def delete(self, request, format=None):
		user = company_offer.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	## Get a filtered list of offers by URL filtering
	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = company_offer.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset = company_offer.objects.all().filter(company_id=query)
		return queryset	

## Viewser for queries
# This will automatically generate a webpage interface along with predefined methods.
# These mehods will allow us to "GET", "PUT", "PATCH" and "DELETE" data.
class QueriesViewSet(viewsets.ModelViewSet):
	## Defines list of queries to be shown
	queryset = query.objects.all()
	## Defines serializer of the Viewset
	serializer_class = QuerySerializer

	## Overrides the "GET" method	
	def get(self, request, format=None):
		users = query.objects.all()
		serializer = QuerySerializer(users, many=True)
		return Response(serializer.data)
	## Overrides the "PUT" method
	def put(self, request, format=None):
		serializer = QuerySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	## Overrides the "DELETE" method
	def delete(self, request, format=None):
		user = query.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	## Get a filtered list of offers by URL filtering
	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = query.objects.all()
		query1 = self.request.GET.get("q")
		if query1:
			queryset = query.objects.all().filter(userid=query1)
		return queryset	

## Viewset for company login
# This will automatically generate a webpage interface along with predefined methods.
# These mehods will allow us to "GET", "PUT", "PATCH" and "DELETE" data.
class CompanyLoginViewSet(viewsets.ModelViewSet):
	## Defines list of queries to be shown
	queryset = company.objects.all()
	## Defines serializer of the Viewset
	serializer_class = CompanyLoginSerializer


## Viewset for companies
# This will automatically generate a webpage interface along with predefined methods.
# These mehods will allow us to "GET", "PUT", "PATCH" and "DELETE" data.
class CompanyViewSet(viewsets.ModelViewSet):
	## Defines serializer of the Viewset
	serializer_class = CompanySerializer

	## Overrides the "GET" method
	def get(self, request, format=None):
		users = company.objects.all()
		serializer = CompanySerializer(users, many=True)
		return Response(serializer.data)

	## Overrides the "PUT" method
	def put(self, request, format=None):
		serializer = CompanySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	## Overrides the "DELETE" method
	def delete(self, request, format=None):
		user = company.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	## Get a filtered list of offers by URL filtering
	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = company.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset = company.objects.all().filter(userid=query)
		return queryset
				
## Viewset for students
# This will automatically generate a webpage interface along with predefined methods.
# These mehods will allow us to "GET", "PUT", "PATCH" and "DELETE" data.
class StudentViewSet(viewsets.ModelViewSet):
	## Defines serializer of the Viewset
	serializer_class = StudentSerializer

	## Overrides the "GET" method
	def get(self, request, format=None):
		users = student.objects.all()
		serializer = StudentSerializer(users, many=True)
		return Response(serializer.data)

	## Overrides the "PUT" method
	def put(self, request, format=None):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	## Overrides the "DELETE" method
	def delete(self, request, format=None):
		user = student.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	## Get a filtered list of offers by URL filtering
	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = student.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset = student.objects.all().filter(userid=query)
		return queryset	

	## Override "PATCH" method to update json
	def patch(self, request):
		serializer = StudentSerializer(data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
		


	
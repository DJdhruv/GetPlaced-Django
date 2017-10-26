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


class OffersViewSet(viewsets.ModelViewSet):
	queryset = company_offer.objects.all()
	serializer_class = OffersSerializer
	def get(self, request, format=None):
		users = company_offer.objects.all()
		serializer = OffersSerializer(users, many=True)
		return Response(serializer.data)

	def put(self, request, format=None):
		serializer = OffersSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		user = company_offer.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = company_offer.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset = company_offer.objects.all().filter(company_id=query)
		return queryset	

class QueriesViewSet(viewsets.ModelViewSet):
	queryset = query.objects.all()
	serializer_class = QuerySerializer	
	def get(self, request, format=None):
		users = query.objects.all()
		serializer = QuerySerializer(users, many=True)
		return Response(serializer.data)

	def put(self, request, format=None):
		serializer = QuerySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		user = query.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = query.objects.all()
		query1 = self.request.GET.get("q")
		if query1:
			queryset = query.objects.all().filter(userid=query1)
		return queryset	

class CompanyLoginViewSet(viewsets.ModelViewSet):
	queryset = company.objects.all()
	serializer_class = CompanyLoginSerializer

class CompanyViewSet(viewsets.ModelViewSet):
	serializer_class = CompanySerializer
	def get(self, request, format=None):
		users = company.objects.all()
		serializer = CompanySerializer(users, many=True)
		return Response(serializer.data)

	def put(self, request, format=None):
		serializer = CompanySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		user = company.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = company.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset = company.objects.all().filter(userid=query)
		return queryset
				

class StudentViewSet(viewsets.ModelViewSet):
	serializer_class = StudentSerializer

	def get(self, request, format=None):
		users = student.objects.all()
		serializer = StudentSerializer(users, many=True)
		return Response(serializer.data)

	def put(self, request, format=None):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		user = student.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = student.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset = student.objects.all().filter(userid=query)
		return queryset	
	def patch(self, request):
		serializer = StudentSerializer(data=request.data, partial=True)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)	
		
class ApplicantsViewSet(viewsets.ModelViewSet):
	queryset = applicant_detail.objects.all()
	serializer_class = ApplicantSerializer	
	def get(self, request, format=None):
		users = applicant_detail.objects.all()
		serializer = ApplicantSerializer(users, many=True)
		return Response(serializer.data)

	def put(self, request, format=None):
		serializer = ApplicantSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		user = applicant_detail.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = applicant_detail.objects.all()
		query1 = self.request.GET.get("q")
		if query1:
			queryset = applicant_detail.objects.all().filter(userid=query1)
		return queryset	



	
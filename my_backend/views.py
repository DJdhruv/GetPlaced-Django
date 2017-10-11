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

class CompanyLoginViewSet(viewsets.ModelViewSet):
	queryset = company.objects.all()
	serializer_class = CompanyLoginSerializer

class CompanyViewSet(viewsets.ModelViewSet):
	serializer_class = CompanySerializer

	def get_queryset(self, *args, **kwargs):
		#queryset = super(CompanyViewSet, self).get_queryset(*args, **kwargs)
		queryset = company.objects.all()
		query = self.request.GET.get("q")
		if query:
			queryset = company.objects.all().filter(userid=query)
		return queryset
				

class StudentViewSet(viewsets.ModelViewSet):
	queryset = student.objects.all()
	serializer_class = StudentSerializer

	def get(self, request, format=None):
		users = student.objects.all()
		serializer = StudentSerializer(users, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = StudentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, format=None):
		user = student.objects.all()
		user.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
		




	
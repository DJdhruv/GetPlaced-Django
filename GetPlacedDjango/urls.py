"""get_placed URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from my_backend import views 
from django.conf import settings
from django.conf.urls.static import static

routerCompanyLogin = routers.DefaultRouter()
routerCompany = routers.DefaultRouter()
routerStudent = routers.DefaultRouter()

routerCompanyLogin.register(r'company',views.CompanyLoginViewSet)
routerCompany.register(r'company',views.CompanyViewSet, 'company')
routerStudent.register(r'student', views.StudentViewSet, 'student')


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', include(routerCompanyLogin.urls)),
    url(r'^companies/', include(routerCompany.urls)),
    url(r'^students/', include(routerStudent.urls)),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#if settings.DEBUG:
 #   urlpatterns+=static(settings.MEDIA_url)
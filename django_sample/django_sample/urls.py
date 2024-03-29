"""django_sample URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django_sample_app import views
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('form/', views.form, name='form'),
    path('ajax_area/', views.add_area_ajax),
    path('ajax_domain/', views.add_domain_ajax),
    path('ajax_feature/', views.add_feature_ajax),
]



# def add_ajax(request):
#     if request.is_ajax():
#         response = {'first-text': 'Lorem Ipsum is simply dummy text', 'second-text': 'to make a type specimen book. It has '}
#
#         return JsonResponse(response)
#     else:
#         raise Http404
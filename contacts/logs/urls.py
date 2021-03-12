from django.urls import path
from . import views
from .views import EmployeeUploadView

urlpatterns =[
    path('', views.index, name='index'),
    path('importemployee/', EmployeeUploadView.as_view(), name='importemployee'),
]
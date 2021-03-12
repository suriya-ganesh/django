from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.views import View
from .models import Log
import io,csv

# Create your views here.
class EmployeeUploadView(View):
    def get(self, request):
        template_name = 'import.html'
        return render(request, template_name)
    def post(self, request):
        user = request.user #get the current login user details
        paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
        portfolio1 = csv.DictReader(paramFile)
        list_of_dict = list(portfolio1)
        objs = [
            Employee(
            first_name=row['first_name'],
            phone_number=row['phone_number'],
            created_by=user, #This is foreignkey value
            updated_by=user, #This is foreignkey value
           
         )
         for row in list_of_dict
     ]
        try:
            msg = Employee.objects.bulk_create(objs)
            returnmsg = {"status_code": 200}
            print('imported successfully')
        except Exception as e:
            print('Error While Importing Data: ',e)
            returnmsg = {"status_code": 500}
       
        return JsonResponse(returnmsg)


def index(request):
    return render(request, 'index.html')


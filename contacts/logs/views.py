from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from datetime import datetime
from django.views import View
from .models import Employee
import io,csv, os

# # Create your views here.
# class EmployeeUploadView(View):
#     def get(self, request):
#         template_name = 'import.html'
#         return render(request, template_name)
#     def post(self, request):
#         user = request.user #get the current login user details
#         paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
#         portfolio1 = csv.DictReader(paramFile)
#         list_of_dict = list(portfolio1)
#         objs = [
#             Employee(
#             first_name=row['first_name'],
#             phone_number=row['phone_number'],
#             created_by=user, #This is foreignkey value
#             updated_by=user, #This is foreignkey value
#
#          )
#          for row in list_of_dict
#      ]
#         try:
#             msg = Employee.objects.bulk_create(objs)
#             returnmsg = {"status_code": 200}
#             print('imported successfully')
#         except Exception as e:
#             print('Error While Importing Data: ',e)
#             returnmsg = {"status_code": 500}
#
#         return JsonResponse(returnmsg)


def upload_csv(request):
    paramFile = io.TextIOWrapper(request.FILES['employeefile'].file)
    portfolio1 = csv.DictReader(paramFile)
    list_of_dict = list(portfolio1)
    print(list_of_dict)


def index(request):
    print(os.path.dirname(os.path.realpath(__file__)))
    # with open(os.path.dirname(os.path.realpath(__file__))+'/employeefile.csv') as csv_file:
    #     csv_reader = csv.reader(csv_file, delimiter=',')
    #     line_count = 0
    #     for row in csv_reader:
    #         if line_count == 0:
    #             print(f'Column names are {", ".join(row)}')
    #             line_count += 1
    #         else:
    #             db_row = Employee(
    #                 name=row[1],
    #                 phone_number=row[2]
    #             )
    #             db_row.save()
    #     print(f'Processed {line_count} lines.')

    return render(request, 'index.html')


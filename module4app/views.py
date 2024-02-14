from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def input(request):
  return render(request, 'input.html')

def details(request):
  name = str(request.GET.get("name"))
  age = int(request.GET.get("age"))
  email = str(request.GET.get("email"))
  town  = str(request.GET.get("town"))
  major = str(request.GET.get('major'))
  semester = str(request.GET.get('semester'))
  year = int(request.GET.get('year'))
  # Check if all fields are filled in
  if not (name and age and email and town and major and semester):
    return HttpResponse("Please fill in all fields.")
  
  context = {
      "name" : name,
      "age" : age,
      "email": email,
      "town" : town,
      "major" : major,
      "semester" : semester,
      "year" : year
  }
  return render(request, 'details.html',context)



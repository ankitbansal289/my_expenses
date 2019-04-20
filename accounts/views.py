from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponse
from accounts.models import expenses
from django.shortcuts import render
from datetime import date, time
from django.db.models import Sum
import datetime

#to get the total sum

# to delete aspecific expense 
def delete (request):
    if request.method == "POST":
        id = int(request.POST.get('id'))
        expense = expenses.objects.get(id =id)
        expense.delete()
    obj = expenses.objects.all()
    sum = expenses.objects.aggregate(Sum('ammount'))
    return render (request,'expenses_details.html',{'obj':obj, 'sum':sum})
    

# function to pull all the records  
def get_expenses(request):
    obj = expenses.objects.all()
    sum = expenses.objects.aggregate(Sum('ammount'))
    return render(request,'expenses_details.html',{'obj':obj,'sum':sum})


#below are the sorting functions
def sort_by_date(request):
    obj = expenses.objects.all().order_by('-date')
    sum = expenses.objects.aggregate(Sum('ammount'))
    return render(request,'expenses_details.html',{'obj':obj,'sum':sum})

def sort_by_ammount_descending(request):
    obj = expenses.objects.all().order_by('-ammount')
    sum = expenses.objects.aggregate(Sum('ammount'))
    return render(request,'expenses_details.html',{'obj':obj,'sum':sum})


def sort_by_ammount_ascending(request):
    obj = expenses.objects.all().order_by('ammount')
    sum = expenses.objects.aggregate(Sum('ammount'))
    return render(request,'expenses_details.html',{'obj':obj,'sum':sum})


def send(request):   # to accept the input od expenses  
    description = request.POST["description"]
    ammount = request.POST["ammount"]
    place = request.POST["place"]
    date = datetime.datetime.now().date()
    time = datetime.datetime.now().time()
    
    exp = expenses()
    x=datetime.datetime.now()
    exp.discription=description
    exp.ammount = ammount
    exp.date = date.today()
    exp.time = x.strftime("%X")
    exp.place = place
    exp.save()
    return render(request,'home.html')

class SignUp(generic.CreateView):  #sign up facility
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'

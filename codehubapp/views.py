from django.shortcuts import render,HttpResponse
from codehubapp.models import Contact
from datetime import date

# Create your views here.
def index(request):
    return render(request,'index.html')
def home(request):
    return render(request,'index.html')
def courses(request):
    return render(request,'courses.html')
def blog(request):
    return render(request,'blog.html')
def contact(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        lastname=request.POST.get('lastname')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        desc=request.POST.get('desc')
        contact=Contact(firstname=firstname,lastname=lastname, email=email, phone=phone, desc=desc,date=date.today())
        contact.save()
    return render(request,'contact.html')


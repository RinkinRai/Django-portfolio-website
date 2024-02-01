from django.shortcuts import render,HttpResponse
from home.models import contact

# Create your views here.
def home(request):
    # return HttpResponse ("This is my homepage (/)")
    context = {'name':'Rinki','course':'Django'}
    return render(request,'home.html',context)

def about(request):
    # return HttpResponse ("This is my about page (/about)")
    return render(request,'about.html')

def projects(request):
#    return HttpResponse ("This is my projects page (/projects)")
    return render(request,'projects.html')

def contact(request):
    if request.method=="Post":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        # print(name,email,phone,desc)
        contact = contact(name=name, email=email, phone=phone,desc=desc)
        contact.save()
        print("The data has been writen to the db")

    # return HttpResponse ("This is my contact page (/contact)")
    return render(request,'contact.html')

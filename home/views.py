from django.shortcuts import render,HttpResponse    
from home.models import Contact

# Create your views here.
def home(request):
    # return HttpResponse("This is my homepage (/)")
    # context={'name':'Harry','course':'Django'}
    return render(request, 'home.html')

def about(request):
    # return HttpResponse("This is my about pahe (/about)")
    return render(request, 'about.html')

def projects(request):
    # return HttpResponse("This is my peojects page (/projects)")
    return render(request, 'projects.html')

def contact (request):
    # return HttpResponse("This is my homepage (/contact)")
    if request.method=="POST":
        # print("This is post")
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        desc=request.POST['desc']
        # m print(name,email,phone,desc)
        contact=Contact(name=name, email=email,phone=phone,desc=desc)
        contact.save()
        print("the data has been written to the db")

    return render(request, 'contact.html')
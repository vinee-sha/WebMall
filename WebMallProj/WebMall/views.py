from django.shortcuts import render,HttpResponse

# Create your views here.
def register(request) :
    return render(request,"register.html")

def login(request) :
    return render(request,"login.html")

def forgotPass(request) :
    return render(request,"forgotPass.html")

def index(request) :
    return render(request,"index.html")

def boys(request) :
    return render(request,"boys.html")  

def boyView(request) :
    return render(request,"boyView.html")

def girls(request) :
    return render(request,"girls.html")  

def girlView(request) :
    return render(request,"girlView.html")

def men(request) :
    return render(request,"men.html")  

def menView(request) :
    return render(request,"menView.html")

def women(request) :
    return render(request,"women.html")  

def womenView(request) :
    return render(request,"womenView.html")

def checkout(request) :
    return render(request,"checkout.html")  

def contact(request) :
    return render(request,"contact.html")  

def faq(request) :
    return render(request,"faq.html")  

def payment(request) :
    return render(request,"payment.html")  
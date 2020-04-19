from django.shortcuts import render
import pyrebase

# Create your views here.
def home(request):
    key = request.GET.get("k",False)
    context={
        "key": key,
    }
    return render(request, "home/index.html", context)

def accounts(request):
    key = request.GET.get("k",False)    
    context={
            "key": key,        
    }
    return render(request, "home/accounts.html", context)


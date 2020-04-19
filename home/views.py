from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "home/index.html")

def accounts(request):
    key = request.GET.get("k",False)    
    context={
            "key": key,        
    }
    return render(request, "home/accounts.html", context)


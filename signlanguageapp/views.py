from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

    
from django.shortcuts import render, redirect
from django.contrib import messages
from signlanguageapp.models import Register



def register(request):

    if request.method == "POST":

        fname = request.POST["fname"]
        lname = request.POST["lname"]
        email = request.POST["email"]
        city = request.POST["city"]
        state = request.POST["state"]
        password = request.POST["password"]
        cpassword = request.POST["cpassword"]

        if Register.objects.filter(email=email).exists():
            messages.error(request, "Email Already Registered")
            return redirect("register")

        if password != cpassword:
            messages.error(request, "Password Does Not Match")
            return redirect("register")

        Register.objects.create(
            fname=fname,
            lname=lname,
            email=email,
            city=city,
            state=state,
            password=password
        )

        return render(request, "success.html")
        #return redirect("login")

    return render(request, "register.html")


def login(request):

    if request.method == "POST":

        email = request.POST["email"]
        password = request.POST["password"]

        try:
            user = Register.objects.get(email=email)

            if user.password == password:

                request.session["user"] = user.id

                messages.success(request, "Login Successfully🎉.")
                return redirect("home")

            else:
                messages.error(request, "Wrong Password")

        except:
            messages.error(request, "Please Register First")
            return redirect("register")

    return render(request, "login.html")


def home(request):

    if "user" not in request.session:
        return redirect("login")

    user = Register.objects.get(id=request.session["user"])

    return render(request, "home.html", {"user": user})


def logout(request):
    request.session.flush()
    return redirect("login")

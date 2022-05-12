from django.shortcuts import render
from .models import *
# Create your views here.

# View for Register Page


def RegisterPage(request):
    return render(request, "app/register.html")


# View for user registration
def UserRegister(request):
    if request.method == "POST":
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        contact = request.POST['contact']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        role = models = request.POST['role']
        # First we will validate that user already exist
        user = User.objects.filter(Email=email)

        if user:
            message = "User already exist"
            return render(request, "app/register.html", {'msg': message})
        else:
            if password == cpassword:
                newuser = User.objects.create(
                    Firstname=fname, Lastname=lname, Email=email, Contact=contact, Password=password, Role=role)
                message = "User register Successfully"
                return render(request, "app/login.html", {'msg': message})
            else:
                message = "Password and Confirm Password Doesnot Match"
                return render(request, "app/register.html", {'msg': message})


# Login VIew

def LoginPage(request):
    return render(request, "app/login.html")


# Login User
def LoginUser(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        # Checking the emailid with database
        user = User.objects.get(Email=email)

        if user:
            if user.Password == password:
                # We are getting user data in session
                rd = User.Role
                if rd == 'doctor' or 'Doctor':
                    request.session['Firstname'] = user.Firstname
                    request.session['Lastname'] = user.Lastname
                    request.session['Role'] = user.Role
                    request.session['Email'] = user.Email
                    return render(request, "app/home.html")
                else:
                    rd = User.Role
                    request.session['Firstname'] = user.Firstname
                    request.session['Lastname'] = user.Lastname
                    request.session['Role'] = user.Role
                    request.session['Email'] = user.Email
                    return render(request, "app/home2.html")
            else:
                message = "Password does not match"
                return render(request, "app/login.html", {'msg': message})
        else:
            message = "User does not exist"
            return render(request, "app/register.html", {'msg': message})

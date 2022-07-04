from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm, UpdateUserForm
from django.contrib.auth import authenticate, login
# Create your views here.
from.models import User
from django.contrib import messages
from django.views.generic import ListView, CreateView, DetailView, View, TemplateView, UpdateView
from django.urls import reverse_lazy



def logout(request):
    
    return redirect("login")

def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('users')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'users/new-user.html', {'form': form, 'msg': msg})


def login_views(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("index2")

            else:
                msg = "invalid credentials"  

        else:
            msg = "errr validating form"      
    return render(request, "accounts/login.html", {"form": form, "msg" : msg})

    """
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("profile")
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'accounts/login.html', {'form': form, 'msg': msg})
"""    
def index2(request):
    context = {
        "index2": index2,
    }
    return render(request, 'index2.html', context)
     
 
 
def profile(request):
    return render(request, "core/profile.html")
     
def users_list(request):
    users_list = User.objects.all()
    context = {
        "users_list": users_list,
        
    }
    return render(request, "users/users.html", context)
"""
def student_users(request):
    student_users = User.objects.filter(user=request.user.Student)
    context = {
        "student_users": student_users,
    }
    return render(request,"users/student_users.html", context)
"""
class UpdateUser(UpdateView):
    model = User
    fields = ("is_admin", "is_active", "is_student", "is_teacher", "first_name", "last_name")
    template_name = "users/update-user.html"
    success_url = reverse_lazy("users") 
"""
def update_user(request, pk):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user, pk=pk)
        

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'User Updated Successfully')
            return redirect(to='users')
    else:
        user_form = UpdateUserForm(instance=request.user)
       

    return render(request, 'users/update-user.html', {'user_form': user_form})

"""    
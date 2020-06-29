from django.contrib.auth import authenticate,login, get_user_model

from django.http import HttpResponse
from django.shortcuts import render,redirect

from . forms import ContactForm,LoginForm,RegisterForm

def login_page(request):
    
    form=LoginForm(request.POST or None)
    context={
        "title":"login form",
        "content": "Welcome to login page",
        "form":form
    }
    print("user logge in as ")
    #print(request.user.is_authenticated())
    if form.is_valid():
        context['form']=LoginForm()
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        password=form.cleaned_data.get('password')
        user = authenticate(request,username=username,password=password)
        print(user)
        #print(request.user.is_authenticated())

        if user is not None:
            #print(request.user.is_authenticated())
            login(request,user)
            #context['form']=LoginForm()
            return redirect('/')
        else:
            print("error")
    return render(request,"auth/login.html",context)
User = get_user_model()
def register_page(request):
    form=RegisterForm(request.POST or None)
    context={
        "title":"hello world",
        "content": "Welcome to register page",
        "form":form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get('username')
        email=form.cleaned_data.get('email')
        password=form.cleaned_data.get('password')
        new_User=User.objects.create_user(username,email,password)
        print("======")
        print(new_User)
    return render(request,"auth/register.html",context)

def home_page(request):
    context={
        "title":"hello world",
        "content": "Welcome to home page",
        
    }
    if request.user.is_authenticated:
        context["premium_content"]="home premium content"
    return render(request,'home_page.html',context)
def about_page(request):
    context={
        "title":"about world",
        "content": "Welcome to about page"
    }
    return render(request,'about_page.html',context)
def contact_page(request):
    contact_form=ContactForm(request.POST or None)
    context={
        "title":"contact world",
        "content": "Welcome to contact page",
        "form":contact_form,
        "brand":"new brand name"
    }
    if contact_form.is_valid():
        print(contact_form.cleaned_data)
   # if request.method=="POST":
      #  print(request.POST)
      #  print(request.POST.get("name"))
  


    return render(request,'contact_page.html',context)
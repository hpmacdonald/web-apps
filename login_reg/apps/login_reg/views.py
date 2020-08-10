from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "new_app/index.html")

def scroll(request):
    return render(request, "new_app/scroll.html")
    
def success(request):
    if "user" not in request.session:
        return redirect("/")
    else:
        print("*1"*50)
        return render(request, "new_app/success.html")

def add_user(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print("*1"*50)
        return redirect("/")
    if request.POST['password'] == request.POST['confirm_password']:
        new_user = User.objects.create(first_name=request.POST['first_name'], 
        last_name=request.POST['last_name'], email=request.POST['email'], password = request.POST['password'])
        request.session['user'] = new_user.first_name
        request.session['id'] = new_user.id
        print("*2"*50)
        return render(request, "new_app/success.html")
    else:
        print("*3"*50)
        return redirect("/")

def login(request):
    context = { 
        "all_messages" : Message.objects.all() 
    }
    logged_user = User.objects.filter(email=request.POST['email'])
    if logged_user[0]:
        if logged_user[0].password == request.POST['password']:
            request.session['user'] = logged_user[0].first_name
            request.session['id'] = logged_user[0].id
            print("*4"*70)
            return render(request, "new_app/profile.html")
        else: 
            print("*5"*50)
            print("something went wrong")
            return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")

# THE WALL STARTING HERE //////////

def adding(request):
    context = { 
        "all_messages" : Message.objects.all() 
    }
    print("8*"*60)
    return render(request, "new_app/profile.html", context)

def process_message(request):
    add_message = Message.objects.create(message=request.POST['add_message'], poster=User.objects.get(id=request.session['id']))
    print("*9"*50)
    return redirect("/add")

def destroy(request, message_id):
    delete_this = Message.objects.get(id=message_id)
    delete_this.delete()
    print("*10"*40)
    return redirect("/add")


def add_comment(request, message_id):
    new_comment = Comment.objects.create(comment=request.POST['comment'], poster=User.objects.get(id=request.session['id']),
    message=Message.objects.get(id=message_id))
    print("*11"*50)
    return redirect("/add")




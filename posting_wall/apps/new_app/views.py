from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "new_app/index.html")
def success(request):
    if "user" not in request.session:
        return redirect("/")
    else:
        context = {
        "all_messages" : Messages.objects.all()
    }
    print("this has worked!")
    print("*6"*50)

    return render(request, "new_app/success.html", context)
    

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
        return redirect("/success")
    else:
        print("*3"*50)
        return redirect("/")

def login(request):
    logged_user = User.objects.filter(email=request.POST['email'])
    if logged_user[0]:
        if logged_user[0].password == request.POST['password']:
            request.session['user'] = logged_user[0].first_name
            request.session['id'] = logged_user[0].id
            print("*4"*70)
            return redirect("/success")
        else: 
            print("*5"*50)
            return redirect("/")

def logout(request):
    request.session.flush()
    return redirect("/")

def messages(request):
    print("request.POST")
    print("*"*50)
    Messages.objects.create(title=request.POST['message_title'], description=request.POST['message_desc'],
    uploaded_by=User.objects.get(id=request.session['id']))
    request.session['title'] = request.POST['message_title']
    request.session['description'] = request.POST['message_desc']
    
    return redirect("/messages")

def profile(request):
    print("*"*50)
    Profile.objects.create(bio=request.POST['bio_user'], 
    uploaded_by=User.objects.get(id=request.session['id']))
    request.session['bio'] = request.POST['bio_user']
    
    return render(request, "new_app/success.html")

def profile_display(request):
    context = {
        "display_profile" : Profile.objects.all()
    }
    print("this has worked!")
    print("*"*50)
    return render(request, "new_app/success.html", context)

def message_display(request):
    context = {
        "all_messages" : Messages.objects.all()
    }
    print("this has worked!")
    print("*"*50)
    return render(request, "new_app/success.html", context)

def view_message(request, my_val):
    context = {
        "one_message" : Messages.objects.get(id=my_val)
    }
    print("this has worked!")
    print("*"*50)
    return render(request, "new_app/message_display.html", context)


def edit(request, my_val):
    edit_this = Messages.objects.get(id=my_val)
    context = {
        "new_edit": edit_this
    }
    return render(request, "new_app/edit.html", context)

def apply_edit(request, my_val):
    the_edit = Messages.objects.get(id=my_val)
    the_edit.title = request.POST['title']
    the_edit.description = request.POST['description']
    the_edit.save()
    print("*10"*50)
    return redirect("/success")


def delete(request, my_val):
    delete_this = Messages.objects.get(id=my_val)
    delete_this.delete()
    print("*6"*50)
    return redirect("/success")

def delete_bio(request, my_val):
    delete_this = Messages.objects.get(id=my_val)
    delete_this.delete()
    print("*6"*50)
    return redirect("/success")


def likes(request, my_val):
    get_this = Messages.objects.get(id=my_val)
    get_this.user_likes.add(User.objects.get(id=request.session['id'])) 
    print("****your post has been liked!*****")
    return redirect("/success")






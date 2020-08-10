from django.shortcuts import render, HttpResponse, redirect
import random
from time import strftime, localtime

#create your views here  
def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'messages' not in request.session:
        request.session['messages'] = []
    return render(request, 'new_app/index.html')


def cavegold(request):
    rand_num = int(random.random() * 5 + 5)
    request.session['gold'] += rand_num
    current_time = strftime("%Y-%m-%d %H:%M %p", localtime())
    request.session['messages'].insert(0,f"You earned ${rand_num} at the caves!({current_time})")
    return redirect('/')
    

def housegold(request):
    rand_num = int(random.random() * 2 + 3)
    request.session['gold'] += rand_num
    current_time = strftime("%Y-%m-%d %H:%M %p", localtime())
    request.session['messages'].insert(0,f"You earned ${rand_num} at the house!({current_time})")
    return redirect('/')

def farmgold(request):
    rand_num = int(random.random() * 10 + 10)
    request.session['gold'] += rand_num
    current_time = strftime("%Y-%m-%d %H:%M %p", localtime())
    request.session['messages'].insert(0,f"You earned ${rand_num} at the farm!({current_time})")
    return redirect('/')

def casinogold(request): 
    rand_num = int(random.random() * 50)
    roll_chance = random.random()
    current_time = strftime("%Y-%m-%d %H:%M %p", localtime())
    if roll_chance > 0.5:
        request.session['gold'] += rand_num
        request.session['messages'].insert(0,f"You earned ${rand_num} at the casino!({current_time})")
    elif roll_chance < 0.5:
        request.session['gold'] -= rand_num
        request.session['messages'].insert(0,f"You lost ${rand_num} at the casino!({current_time})")
    return redirect('/')

def clear(request):
    request.session.flush() 
    print("**item deleted**")
    return redirect('/')
            

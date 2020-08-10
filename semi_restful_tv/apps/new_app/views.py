from django.shortcuts import render, HttpResponse, redirect
from .models import Show

def index(request):
    return render(request, "new_app/index.html")

def create(request):
    print(request.method)
    errors = Show.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        print("*"*25, "*"*25)
        return redirect("/")
    if request.method == "POST":
        print(request.POST)
        print("*"*50)
        Show.objects.create(title=request.POST['show_title'], network=request.POST['show_network'], 
        release_date=request.POST['show_release'])
        request.session['title'] = request.POST['show_title']
        request.session['network'] = request.POST['show_network']
        request.session['release'] = request.POST['show_release']
    return redirect("/shows")
    

def shows(request):
    context = {
        "all_shows" : Show.objects.all()
    }
    print("this has worked!")
    print("*"*50)
    return render(request, "new_app/shows.html", context)

def edit(request, my_val):
    edit_this = Show.objects.get(id=my_val)
    edit = {
        "new_edit": edit_this
    }
    return render(request, "new_app/edit.html", edit)

def process_edit(request, my_val):
    the_edit = Show.objects.get(id=my_val)
    the_edit.title = request.POST['title']
    the_edit.network = request.POST['network']
    the_edit.release_date = request.POST['release_date']
    the_edit.save()
    print("*10"*50)
    return redirect("/shows")

def show_individual(request, my_val):
    context = {
        "show_id" : Show.objects.get(id=my_val),
        "all_shows" : Show.objects.all()
    }
    print("*"*69)
    return render(request, "new_app/show_each.html", context)

def delete(request, my_val):

    delete_this = Show.objects.get(id=my_val)
    delete_this.delete()
    print("*6"*50)
    return redirect("/shows")


   # quantity_from_form = int(request.POST["quantity"])
    # price_from_form = float(request.POST["price"])
    # total_charge = quantity_from_form * price_from_form
    # # add_taxes = total_charge * 0.06
    # # final_price = taxes + total_charge
    # if price_from_form < 0:
    #     print("*1"*50)
    #     return redirect("/")
    # if quantity_from_form < 0:
    #     print("*2"*50)
    #     return redirect("/")
    new_order = Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
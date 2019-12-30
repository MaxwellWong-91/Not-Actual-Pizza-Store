from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import *
from itertools import chain

# Create your views here.
def home(request):
    return (render(request, "home.html"))

def menu(request):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))
    context = {
        "foodCategory": FoodCategory.objects.all(),
    }

    return (render(request, "menu.html", context))

def pizza(request):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))
    return (render(request, "pizza.html"))


def topping(request, pizza):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))

    context = {
        "toppings": Topping.objects.all(),
        "name": pizza
    }
    
    return (render(request, "topping.html", context))

def subs(request):

    if (not request.user.is_authenticated):
        return (render(request, "error.html"))

    context = {
        "subs": SubType.objects.all(),
    }

    
    return (render(request, "subs.html", context))

def addons(request, subs):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))
    
    context = {
        "addons": AddOn.objects.all(),
        "currSub": SubType.objects.get(name = subs)
    }

    return (render(request, "addon.html", context))

def pasta(request):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))

    context = {
        "pastas": PastaType.objects.all()
    }

    return (render(request, "pasta.html", context))

def salads(request):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))

    context = {
        "salads": SaladType.objects.all()
    }
    return (render(request, "salads.html", context))

def platters(request):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))

    context = {
        "platters": PlatterType.objects.all()
    }

    return (render(request, "platters.html", context))

def platterSize(request, platter):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))

    context = {
        "currPlatter": PlatterType.objects.get(name = platter)
    }

    return (render(request, "size.html", context))

def order(request):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))

    # get the current user
    currUser = request.user

    try: 
        currOrder = Order.objects.get( user = currUser )
    except Order.DoesNotExist:
        currOrder = Order( user = currUser )
    currOrder.save()


    if (request.method == "POST"):
        # should always have a category and name for all orders
        category = request.POST.get("category")
        name = request.POST.get("name")

        # handle pizza order
        if category == "Pizza":
            # remove the '/' char from name
            name = name[:-1]
            toppings = request.POST.getlist("topping")
            size = request.POST.get("size")
            # create the pizza
            orderToAdd = Pizza( regular = True if name == "regular" else False, size = size )

            orderToAdd.save()

            # add the topping
            for topping in toppings:
                orderToAdd.toppings.add( Topping.objects.get(name = topping) )

            # set price 
            orderToAdd.price = orderToAdd.getPrice()

            orderToAdd.save()

            # add to order
            currOrder.pizza.add(orderToAdd)

        # handle subs order
        elif category == "Subs":
            addons = request.POST.getlist("addon")
            # the try except is bc one of the subs has no small option
            try:
                size = request.POST.get("size")
            except:
                size = "Large"
            
            # create the subs
            orderToAdd = Subs( size = size )

            orderToAdd.save()

            orderToAdd.name.add( SubType.objects.get(name = name) )

            orderToAdd.save()

            # add the addon
            for addon in addons:
                orderToAdd.addons.add( AddOn.objects.get(name = addon) )
            
            # set price 
            orderToAdd.price = orderToAdd.getPrice()

            orderToAdd.save()

            # add to order
            currOrder.subs.add(orderToAdd)

        # handle pasta order
        elif category == "Pasta":
            pasta = PastaType.objects.get(name = name)
            # create the pasta
            orderToAdd = Pasta( price = pasta.price )

            orderToAdd.save()

            orderToAdd.name.add(pasta)

            # add to order
            currOrder.pasta.add(orderToAdd)

        # handle salad order
        elif category == "Salad":
            salad = SaladType.objects.get(name = name)
            # create the salad
            orderToAdd = Salad( price = salad.price )

            orderToAdd.save()

            orderToAdd.name.add(salad)

            # add to order
            currOrder.salad.add(orderToAdd)

        # handle platter order
        elif category == "Platters":
            size = request.POST.get("size")

            # create the platter
            orderToAdd = Platters(size = size)

            orderToAdd.save()

            platter = PlatterType.objects.get(name = name)

            orderToAdd.name.add(platter)

            # set price 
            orderToAdd.price = orderToAdd.getPrice()

            orderToAdd.save()

            # add to order
            currOrder.platters.add(orderToAdd)

    # collect all the orders
    allOrder = list(chain(currOrder.pizza.all(), currOrder.subs.all(), currOrder.pasta.all(), currOrder.salad.all(), currOrder.platters.all()))

    context = {
        "allOrder": allOrder,
        "total": currOrder.getPrice()
    }

    return (render(request, "order.html", context))


def cancelOrder(request):
    id = request.POST.get("id")
    category = request.POST.get("type")
    
    currOrder = Order.objects.get( user = request.user )
    
    # use getattr to access model fields, then use the id to find the item
    item = getattr(currOrder, category).get(id = id)

    # remove the relationship with order
    getattr(currOrder, category).remove(item)

    # delete the order
    item.delete()

    return (JsonResponse({"price": currOrder.getPrice()}))

def purchase(request):
    if (not request.user.is_authenticated):
        return (render(request, "error.html"))

    currOrder = Order.objects.get( user = request.user )

    allOrder = list(chain(currOrder.pizza.all(), currOrder.subs.all(), currOrder.pasta.all(), currOrder.salad.all(), currOrder.platters.all()))

    # remove all relationship in the order and the item
    for item in allOrder:
        
        getattr(currOrder, item.getType() ).remove(item)
        
        item.delete()
        
    # delete the order itself
    currOrder.delete()
    
    return (render(request, "purchase.html"))
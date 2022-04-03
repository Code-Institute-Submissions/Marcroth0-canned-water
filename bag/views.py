from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect

def view_bag(request):
    """A view that renders the bag page"""
    
    return render(request, 'bag/bag.html')

def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

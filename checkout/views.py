from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "sorry, your bag is empty!")
        return redirect(reverse('products'))

    template = 'checkout/checkout.html'
    order_form = OrderForm()

    context = {
        'order_form': order_form,
    }

    return render(request, template, context)

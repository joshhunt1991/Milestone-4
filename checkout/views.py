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
        'stripe_public_key': 'pk_test_51Ida2xAXeR7kMTtwdL7G4r4otFowJFrhjJ3uaWGKEY3tBsJZ1vyWGssOj7tDrqzV59mhr2fPnz1qOj2TEkkTyREj00HfuDaXWg',  # noqa
        'client_secret': 'test client secret',
        'order_form': order_form,
    }

    return render(request, template, context)

from django.shortcuts import (render, redirect, reverse,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product

# Create your views here.


def view_bag(request):
    """ renders the bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ adds the selected items to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    product = Product.objects.get(pk=item_id)
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    messages.success(request, f'Added {product.name} to your bag')

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """function for adjusting product quantity in the bag"""

    quantity = int(request.POST.get('quantity'))
    product = get_object_or_404(Product, pk=item_id)
    bag = request.session.get('bag', {})

    if quantity > 0:
        messages.success(
            request, f'Updated {product.name} quantity to {bag[item_id]}')
        bag[item_id] = quantity
    else:
        messages.success(request, f'Removed {product.name} from your bag')
        bag.pop(item_id)

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """delete items from bag"""

    product = get_object_or_404(Product, pk=item_id)

    try:
        bag = request.session.get('bag', {})

        bag.pop(item_id)
        messages.success(request, f'Removed {product.name} from your bag')
        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)

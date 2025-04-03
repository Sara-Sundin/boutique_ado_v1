from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment")
        return redirect(reverse('products'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51R9h08CTmqXXhmcza7n6e7Nct6cThiso4dpnVi9tUgwxIo6uMvlpG9V1Z89bgbgrCMLKICUOTR1TtMIerRtw1Q9o006kaLYgOZ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
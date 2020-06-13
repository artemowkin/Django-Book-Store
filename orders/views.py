import stripe

from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import PermissionDenied
from django.http import HttpResponseNotAllowed

stripe.api_key = settings.STRIPE_TEST_SECRET_KEY


def charge(request):
    if not request.user.is_authenticated:
        raise PermissionDenied

    if request.method == 'POST':
        charge = stripe.Charge.create(
            amount=request.POST['stripeAmount'],
            currency='usd',
            description=request.POST['stripeDescription'],
            source=request.POST['stripeToken'],
        )
        return render(request, 'orders/charge.html')

    return HttpResponseNotAllowed(['POST'], '<h1>405 Method Not Allowed</h1>')

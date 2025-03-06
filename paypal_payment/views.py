from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model
from paypal.standard.forms import PayPalPaymentsForm
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from orders.models import Order
from base.models import Base

import uuid

User = get_user_model()

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    total_price = request.data.get("total_price")
    cart = request.data.get("cart")

    transaction_id = str(uuid.uuid4())
    user = User.objects.filter(id=1).first()

    for item in cart:
        product = Base.objects.filter(id=item['id']).first()
        Order.objects.create(transaction_id=transaction_id, user=user, item=product)


    # PayPal payment details
    paypal_dict = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': str(total_price),
        'item_name': "Addmesh-Product",
        'invoice': transaction_id,
        'currency_code': 'USD',
        'notify_url': request.build_absolute_uri(reverse('paypal-ipn')),
        'return_url': request.build_absolute_uri('/payment/success/'),
        'cancel_return': request.build_absolute_uri('/payment/cancel/'),
    }

    
    # Decide whether to use Sandbox or Live PayPal URL
    paypal_base_url = "https://www.sandbox.paypal.com" if settings.PAYPAL_TEST else "https://www.paypal.com"

    # Construct the PayPal URL with GET parameters
    paypal_url = paypal_base_url + f"/cgi-bin/webscr?cmd=_xclick&business={paypal_dict['business']}&amount={paypal_dict['amount']}&item_name={paypal_dict['item_name']}&invoice={paypal_dict['invoice']}&currency_code={paypal_dict['currency_code']}&notify_url={paypal_dict['notify_url']}&return={paypal_dict['return_url']}&cancel_return={paypal_dict['cancel_return']}"

    return Response({'redirect_url': paypal_url}, status=status.HTTP_200_OK)

from django.conf import settings
from django.dispatch import receiver
from paypal.standard.ipn.signals import valid_ipn_received
from .models import PayPalTransaction
from orders.models import Order
from base.models import Base
from my_shelf.models import MyShelf


@receiver(valid_ipn_received)
def paypal_payment_received(sender, **kwargs):
    ipn = sender

    print(ipn.payment_status)

    if ipn.payment_status == "Completed":
        if ipn.receiver_email != settings.PAYPAL_RECEIVER_EMAIL:
            return  # Ignore invalid payments

        try: 
            orders = Order.objects.filter(transaction_id=ipn.invoices)

            for order in orders:
                user = order.user
                item_id = order.item.id
                product = Base.objects.filter(id=item_id).first()

                if not order.paid:
                    order.paid = True
                    order.save()
                    MyShelf.create(user=user, item=product)

        except Order.DoesNotExist: 
            return print({"error": "Order Not Found!"})
            

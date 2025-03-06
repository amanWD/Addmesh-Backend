from django.urls import path, include
from .views import create_order

urlpatterns = [
    path('paypal/create-order/', create_order, name='create-order'),
    path('paypal/ipn/', include('paypal.standard.ipn.urls')),  # IPN listener
]

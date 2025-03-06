from djoser.views import UserViewSet
from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import CustomLoginSerializer


class CustomUserViewSet(UserViewSet):
    def perform_create(self, serializer):
        user = serializer.save()
        user.set_activation_code()
        self.send_activation_code(user)
    
    def send_activation_code(self, user):
        if user.preferred_contact == "email":
            self.send_email_activation(user)
        elif user.preferred_contact == "phone" and user.phone_number:
            self.send_sms_activation(user)

    def send_email_activation(self, user):
        subject = "Your Activation Code"
        message = f"Your activation code is: {user.activation_code}"
        send_mail(subject, message, "ammannuel5@gmail.com", [user.email])

    def send_sms_activation(self, user):
        client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_KEY)

        message = client.messages.create(
            body=f"Your activation code is: {user.activation_code}",
            messaging_service_sid=settings.TWILIO_MESSAGING_SERVICE_SID, 
            to=user.phone_number
        )


class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomLoginSerializer


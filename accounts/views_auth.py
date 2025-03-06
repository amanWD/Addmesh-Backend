from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from twilio.rest import Client
from django.conf import settings
import random
import string

def generate_activation_code():
    return ''.join(random.choices(string.digits, k=6))

User = get_user_model()

@api_view(["POST"])
@permission_classes([AllowAny])
def activate_account(request):
    activation_code = request.data.get("activation_code")
    try: 
        user = User.objects.get(activation_code=activation_code, is_active=False)
        user.is_active = True
        user.activation_code = None
        user.save()

        return Response({"message": "Account activated successfully"}, status=status.HTTP_200_OK)
    except User.DoesNotExist:
        return Response({"error": "Invalid activation code"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@permission_classes([AllowAny])
def resend_activation_code(request):
    email_or_phone = request.data.get("email_or_phone")

    try:
       activation_code = generate_activation_code()

       user = User.objects.filter(email=email_or_phone).first() or User.objects.filter(phone_number=email_or_phone).first()

       user.activation_code = activation_code 
       user.save()
       
       if user.preferred_contact == "email":
        return send_email_activation(user)
       
       elif user.preferred_contact == "phone":
        return send_sms_activation(user)

       else:
        return Response({"error": "Email or phone number is required "}, status=status.HTTP_400_BAD_REQUEST)
       
    except User.DoesNotExist:
        return Response({"error": "User not found or already active"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@permission_classes([AllowAny])
def reset_password(request):
    email_or_phone = request.data.get("email_or_phone")

    try:
       activation_code = generate_activation_code()
       
       if User.objects.filter(email=email_or_phone).first():
        user = User.objects.filter(email=email_or_phone).first()

        user.activation_code = activation_code 
        user.save()

        return send_email_activation(user)
       
       elif User.objects.filter(phone_number=email_or_phone).first():
        user = User.objects.filter(phone_number=email_or_phone).first()
        
        user.activation_code = activation_code 
        user.save()
        return send_sms_activation(user)

       else:
        return Response({"error": "Email or phone number is required "}, status=status.HTTP_400_BAD_REQUEST)
       
    except User.DoesNotExist:
        return Response({"error": "User not found or already active"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@permission_classes([AllowAny])
def reset_password_confirm(request):
    email_or_phone = request.data.get("email_or_phone")
    code = request.data.get("code")
    new_password = request.data.get("new_password")
    re_new_password = request.data.get("re_new_password")

    try:
       user = User.objects.filter(email=email_or_phone).first() or User.objects.filter(phone_number=email_or_phone).first()
       
       if user.activation_code == code:
          if new_password == re_new_password:
            user.set_password(new_password)
            user.activation_code = None
            user.save()

            return Response({"message": "Password reset was successfully"}, status=status.HTTP_200_OK)
          else:
             return Response({"error": "New password and ReNew password are not equal"}, status=status.HTTP_400_BAD_REQUEST)

       else:
        return Response({"error": "Incorrect Code"}, status=status.HTTP_400_BAD_REQUEST)
       
    except User.DoesNotExist:
        return Response({"error": "User not found or already active"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def transfer_account(request):
    new_email_or_phone = request.data.get("new_email_or_phone")
    current_password = request.data.get("current_password")
    transfer_type = request.data.get("transfer_type")

    try:
       user = request.user
       activation_code = generate_activation_code()

       if user.check_password(current_password):
        user.activation_code = activation_code
        user.save()

        if transfer_type == "email":
            return send_email_activation(user, new_email_or_phone)
        
        elif transfer_type == "phone":
            return send_sms_activation(user, new_email_or_phone)

        else:
            return Response({"error": "Email or phone number is required "}, status=status.HTTP_400_BAD_REQUEST)
       else:
          return Response({"error": "Incorrect Password"}, status=status.HTTP_403_FORBIDDEN)
       

    except User.DoesNotExist:
        return Response({"error": "User not found or already active"}, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def transfer_account_confirm(request):
    new_email_or_phone = request.data.get("new_email_or_phone")
    code = request.data.get("code")
    transfer_type = request.data.get("transfer_type")

    try:
       user = request.user

       if user.activation_code == code:
        if transfer_type == "email":
            user.email = new_email_or_phone
            user.activation_code = None
            user.save()

            return Response({"message": "Email was transferred successfully"}, status=status.HTTP_200_OK)
        
        elif transfer_type == "phone":
            user.phone_number = new_email_or_phone
            user.activation_code = None
            user.save()

            return Response({"message": "Phone was transferred successfully"}, status=status.HTTP_200_OK)

        else:
            return Response({"error": "Email or phone number is required "}, status=status.HTTP_400_BAD_REQUEST)
       else:
          return Response({"error": "Incorrect Code"}, status=status.HTTP_403_FORBIDDEN)
       

    except User.DoesNotExist:
        return Response({"error": "User not found or already active"}, status=status.HTTP_400_BAD_REQUEST)
    
def send_email_activation(user, email=None):
    subject = "Your Activation Code"
    message = f"Your activation code is: {user.activation_code}"
    
    if email: 
       send_mail(subject, message, "ammannuel5@gmail.com", [email])
    else:
       send_mail(subject, message, "ammannuel5@gmail.com", [user.email])

    return Response({"message": "Activation code via email"}, status=status.HTTP_200_OK)


def send_sms_activation(user, phone_number=None):
    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_KEY)

    if phone_number:
       message = client.messages.create(
        body=f"Your activation code is: {user.activation_code}",
        messaging_service_sid=settings.TWILIO_MESSAGING_SERVICE_SID, 
        to=phone_number
    )
    else:
       message = client.messages.create(
        body=f"Your activation code is: {user.activation_code}",
        messaging_service_sid=settings.TWILIO_MESSAGING_SERVICE_SID, 
        to=user.phone_number
    )

    return Response({"message": "Activation code via SMS"}, status=status.HTTP_200_OK)

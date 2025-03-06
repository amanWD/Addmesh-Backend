from djoser.serializers import UserCreateSerializer, SetPasswordSerializer
from accounts.models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'name', 'phone_number', 'preferred_contact', 'email', 'password')


class CustomLoginSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        email_or_phone = attrs.get("email")
        password = attrs.get("password")

        if not email_or_phone or not password:
            raise AuthenticationFailed("Both fields are required")
        
        user = CustomUser.objects.filter(email=email_or_phone).first() or CustomUser.objects.filter(phone_number=email_or_phone).first()

        if not user:
            raise AuthenticationFailed("User not found")
        
        if not user.check_password(password):
            raise AuthenticationFailed("Wrong Credentials")
        
        if not user.is_active:
            raise AuthenticationFailed("User account is not active")
        
        return super().validate({"email": user.email, "password": password})

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['name'] = user.name
        token['email'] = user.email
        token['phone_number'] = user.phone_number
        token['is_admin'] = user.is_admin

        return token
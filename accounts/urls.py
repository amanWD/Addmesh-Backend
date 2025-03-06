from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet, CustomLoginView
from .views_auth import activate_account, resend_activation_code, transfer_account, transfer_account_confirm, reset_password, reset_password_confirm

router = DefaultRouter()
router.register(r'users', CustomUserViewSet)

urlpatterns = [
    path('auth/', include(router.urls)),
    path('auth/activate/', activate_account, name="activate-account"),
    path('auth/resend-activation/', resend_activation_code, name="resend-activate-code"),
    path('auth/jwt/create/', CustomLoginView.as_view(), name="custom_jwt_create"),
    path('auth/transfer-account/', transfer_account, name="transfer-account"),
    path('auth/transfer-account-confirm/', transfer_account_confirm, name="transfer-account-confirm"),
    path('auth/reset-password/', reset_password, name="reset-password"),
    path('auth/reset-password-confirm/', reset_password_confirm, name="reset-password-confirm"),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
import string

def generate_activation_code():
    return ''.join(random.choices(string.digits, k=6))


class CustomUserManager(BaseUserManager):
    def create_user(self, email, name, phone_number=None, preferred_contact="email", password=None, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            phone_number=phone_number,
            preferred_contact=preferred_contact,
            is_admin=is_admin
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, phone_number=None, preferred_contact="email", password=None, is_admin=True):
        user = self.create_user(
            email=email,
            password=password,
            name=name,
            phone_number=phone_number,
            preferred_contact=preferred_contact,
            is_admin=is_admin,
        )

        user.is_admin = True

        user.save(using=self._db)
        return user


class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=35, blank=True, null=True, unique=True)

    activation_code = models.CharField(max_length=6, blank=True, null=True)
    PREFERENCE_CHOICE = (("email", "Email"), ("phone", "Phone"))
    preferred_contact = models.CharField(max_length=10, choices=PREFERENCE_CHOICE, default="email")

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'is_admin', 'phone_number', 'preferred_contact']

    objects = CustomUserManager()

    def get_full_name(self):
        return self.name

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
    def set_activation_code(self):
        self.activation_code = generate_activation_code()
        self.save()

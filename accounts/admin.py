from django.contrib import admin
from accounts.models import CustomUser
from django.contrib.auth.admin import UserAdmin



class CustomUserAdmin(UserAdmin):
    list_display = [
        "id",
        "email",
        "name",
        "phone_number",
        "is_active",
        "is_admin",
        "preferred_contact",
    ]
    list_filter = ('is_admin', )
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone_number','preferred_contact')}),
        ('Permissions', {'fields': ('is_admin', 'is_active')})
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'phone_number', 'preferred_contact', 'password', 'password2'),
        })
    )

    search_fields = ('email', )
    ordering = ('email', 'id')
    filter_horizontal = ()


admin.site.register(CustomUser, CustomUserAdmin)
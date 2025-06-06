from django.contrib.auth.forms import UserChangeForm, AdminUserCreationForm

from .models import CustomUser

class CustomUserCreationForm(AdminUserCreationForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (
            "username",
            "email",
        )
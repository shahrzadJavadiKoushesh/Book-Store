from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# UserCreationForm for signup
# UserChangeForm for admin

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ('age',)
        #         username + password1 + password2 + age
        fields = ('username', 'age', 'email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'age', 'email',)

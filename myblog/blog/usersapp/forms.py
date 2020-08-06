from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import BlogUser


class RegistrationForm(UserCreationForm):
    class Meta:
        model = BlogUser
        fields = ('username', 'password1', 'password2', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

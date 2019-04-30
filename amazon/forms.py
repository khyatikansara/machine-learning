from django.forms import ModelForm
from amazon.models import Register
from django.contrib.auth.models import User

class RegisterForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','password','email']

class LoginForm(ModelForm):
    class Meta:
        model = Register
        fields = []
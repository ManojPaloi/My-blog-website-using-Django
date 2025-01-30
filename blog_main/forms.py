from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):  # Corrected class name
    class Meta:  # Corrected "meta" to "Meta"
        model = User
        fields = ('email', 'username', 'password1', 'password2')

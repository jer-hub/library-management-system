from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate
from django.core.exceptions import ValidationError
from customuserauth.models import CustomUserModel

User = get_user_model()

class CustomAuthenticationForm(AuthenticationForm):     
    username = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )
    password = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )


    class Meta:
        model = User
        fields = ['username', 'password']

        def clean(self):
            cleaned_data = super().clean()
            email = cleaned_data.get('email')
            password = cleaned_data.get('password')

            if email and password:
                user = authenticate(username=email, password=password)
                if user is None:
                    raise forms.ValidationError('Invalid email or password')
            else:
                raise forms.ValidationError('Both email and password are required')
            
            return cleaned_data


class RegisterForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )
    username = forms.CharField(
        required=True,
        max_length=255,
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )
    first_name = forms.CharField(
        required=True,
        max_length=255,
        label="First Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        required=True,
        max_length=255,
        label="Last Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )
    password1 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Password"}
        ),
    )
    password2 = forms.CharField(
        required=True,
        label="Password",
        widget=forms.PasswordInput(
            attrs={"class": "form-control", "placeholder": "Confirm Password"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exists():
            raise ValidationError("Username already exists.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error("password2", "Passwords do not match.")

        return cleaned_data
    
class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "Email"}),
    )
    username = forms.CharField(
        required=True,
        max_length=255,
        label="Username",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Username"}
        ),
    )
    first_name = forms.CharField(
        required=True,
        max_length=255,
        label="First Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        required=True,
        max_length=255,
        label="Last Name",
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exclude(pk=self.user.pk).exists():
            raise ValidationError("Email already exists.")
        return email

    def clean_username(self):
        username = self.cleaned_data.get("username")
        if User.objects.filter(username=username).exclude(pk=self.user.pk).exists():
            raise ValidationError("Username already exists.")
        return username

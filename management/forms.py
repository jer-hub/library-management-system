from django.forms import ModelForm
from django import forms
from management.models import Book, Department
from django.contrib.auth import get_user_model

User=get_user_model()

class BookForm(ModelForm):

    title = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={"class": "form-control", "placeholder": "title"}),
    )

    author = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "author"}
        ),
    )

    call_number = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "call number",
            }
        ),
    )
    pages = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(
            attrs={
                "type": "number",
                "class": "form-control",
                "placeholder": "pages",
            }
        ),
    )
    place_of_publication = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "place of publication"}
        ),
    )
    publisher = forms.CharField(
        required=True,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "publisher"}
        ),
    )

    copyright_date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={"type": "date", "class": "form-control"}),
    )

    department = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=True,
        widget=forms.Select(attrs={"class": "form-control"}),
    )

    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "call_number",
            "place_of_publication",
            "department",
            "publisher",
            "copyright_date",
            "pages",
        ]

class DepartmentForm(ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={
        "class":"form-control",
        "placeholder": "name of department"
    }))
    class Meta:
        model = Department
        fields = ("name",)

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
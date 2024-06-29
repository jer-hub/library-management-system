from dataclasses import fields
from django import forms

from management.models import Department


class SearchForm(forms.Form):
    search = forms.CharField(
        max_length=256,
        required=False,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Search title of the book"}
        ),
    )

    class Meta:
        field = ("search",)


class FilterForm(forms.Form):
    dept_select = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        widget=forms.Select(
            attrs={"class": "form-select"},
        ),
    )

    class Meta:
        field = ("dept_select",)

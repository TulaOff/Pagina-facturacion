from django import forms


class NameForm(forms.Form):
    cuit = forms.IntegerField(required=False)

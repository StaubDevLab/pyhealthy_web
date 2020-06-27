from django import forms


class ConnexionForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=30, label_suffix='')
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, label_suffix='')


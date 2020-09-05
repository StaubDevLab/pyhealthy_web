from django import forms


class ConnexionForm(forms.Form):
    email = forms.EmailField(label='E-mail', max_length=30, label_suffix='')
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, label_suffix='')


class InscriptionForm(forms.Form):
    surname = forms.CharField(label='Nom', max_length=30, label_suffix='')
    firstname = forms.CharField(label='Prénom', max_length=30, label_suffix='')
    email = forms.EmailField(label='E-mail', max_length=30, label_suffix='')
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, label_suffix='')
    password_confirm = forms.CharField(label="Confirmer le mot de passe", widget=forms.PasswordInput, label_suffix='')

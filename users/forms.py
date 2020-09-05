from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser
from snowpenguin.django.recaptcha3.fields import ReCaptchaField


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields


class UserForm(forms.ModelForm):
    password_signup = forms.CharField(widget=forms.PasswordInput(), label='Mot de passe')
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label='Répéter mot de passe')

    class Meta:
        model = CustomUser
        fields = ('email', 'password_signup')

    def clean(self):
        cleaned_data = super(UserForm, self).clean()
        print(cleaned_data)
        password_signup = cleaned_data.get("password_signup")
        confirm_password = cleaned_data.get("confirm_password")

        if password_signup != confirm_password:
            raise forms.ValidationError(
                "Le mot de passe et la confirmation ne correspondent pas."
            )
        return cleaned_data

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password_signup"])
        if commit:
            user.save()
        return user


class ConnexionForm(forms.Form):
    class Meta:
        model = CustomUser

    username = forms.CharField(label='Adresse e-mail ou username', max_length=30, label_suffix='')
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput, label_suffix='', )

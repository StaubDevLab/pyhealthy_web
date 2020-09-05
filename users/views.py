from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from users.forms import ConnexionForm, CustomUserCreationForm, UserForm
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from users.utils_users import translate_check_password, create_username


# Create your views here.
def ajax_login(request):
    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return HttpResponse()
            else:  # sinon une erreur sera affichée
                error = True
                return JsonResponse({"error": error}).__setattr__('status_code', 403)

    else:
        return redirect(request, 'home')


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            username = form.cleaned_data["email"]
            password = form.cleaned_data["password_signup"]
            try:
                validate_password(password)
            except ValidationError as e:
                form.add_error('password_signup', e)
                response = JsonResponse({"error": "there was an error", 'formErrors': {
                    "password": translate_check_password(dict(form.errors)['password_signup'])}})
                response.status_code = 403  # To announce that the user isn't allowed to publish
                return response
            form.save()
            create_username(username)
            user = authenticate(username=username, password=password)  # Nous vérifions si les données sont correctes
            if user:  # Si l'objet renvoyé n'est pas None
                login(request, user)  # nous connectons l'utilisateur
                return HttpResponse()
            else:  # sinon une erreur sera affichée
                response = JsonResponse({"error": "there was an error", 'formErrors': form.errors})
                response.status_code = 403  # To announce that the user isn't allowed to publish
                return response
        else:
            response = JsonResponse({"error": "there was an error", 'formErrors': form.errors})
            response.status_code = 403  # To announce that the user isn't allowed to publish
            return response
    else:
        return redirect('home')


def ajax_logout(request):
    logout(request)
    return redirect('home')

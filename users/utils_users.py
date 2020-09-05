import random
from users.models import CustomUser


def translate_check_password(errors):
    trans_errors = []
    for error in errors:
        if 'digit' in error:
            trans_errors.append("Le mot de passe requiert au moins 1 nombre")
        elif 'letters' in error:
            trans_errors.append("Le mot de passe requiert au moins 9 lettres")
        elif 'upper' in error:
            trans_errors.append("Le mot de passe requiert au moins 1 lettre majuscule")
        elif 'lower' in error:
            trans_errors.append("Le mot de passe requiert au moins 1 lettre minuscule")
    if len(trans_errors) > 1:
        trans_errors = "Le mot de passe requiert encore au moins" + ",".join(
            ["".join(e.split('Le mot de passe requiert au moins')) for e in trans_errors]) + "."
    return trans_errors


def create_username(e):
    concat = e.split('@')[0].split('.')
    username_created = "#"
    for x in concat:
        username_created += x[0]
    username_created += str(random.randint(1, 1000000))
    u = CustomUser.objects.get(email=e)
    print(u)
    u.username = username_created
    u.save()

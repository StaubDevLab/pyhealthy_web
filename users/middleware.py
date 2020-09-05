from django.contrib import messages
from datetime import timedelta
from django.utils import timezone
from users.models import CustomUser


def messages_middleware(get_response):
    def middleware(request):

        response = get_response(request)
        if request.user.is_authenticated:
            if request.user.date_joined + timedelta(seconds=20) > timezone.now():
                messages.info(request, f"Inscription validée! {request.user.username}")
            elif request.user.last_login + timedelta(seconds=20) > timezone.now() > request.user.date_joined + timedelta(seconds=20):
                messages.info(request, f"{request.user.username}")

        return response

    return middleware

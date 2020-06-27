from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, JsonResponse
from django.views.generic import TemplateView
from .forms import ConnexionForm


class HomePage(TemplateView):
    template_name = 'general/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomePage, self).get_context_data(**kwargs)
        context['form'] = {'login': ConnexionForm}
        return context

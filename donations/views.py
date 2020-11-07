from django.shortcuts import render
from django.views.generic import TemplateView, View
from django.db.models import Sum

from .models import Donation


class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        donated_bags = Donation.objects.aggregate(Sum('quantity'))
        if donated_bags['quantity__sum'] is None:
            donated_bags['quantity__sum'] = 0
        institutions_supported = Donation.objects.values('institution').distinct().count()
        ctx = {
            'donated_bags': donated_bags['quantity__sum'],
            'institutions_supported': institutions_supported,
        }
        return render(request, 'index.html', ctx)


class AddDonationView(TemplateView):
    template_name = 'form.html'


class LoginView(TemplateView):
    template_name = 'login.html'


class RegisterView(TemplateView):
    template_name = 'register.html'


class ConfirmationView(TemplateView):
    template_name = 'form-confirmation.html'

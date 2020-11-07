from django.shortcuts import HttpResponse, redirect, render
from django.views.generic import TemplateView, View
from django.db.models import Sum
from django.contrib.auth import authenticate, get_user_model, login
from django.contrib.auth.views import LogoutView
from django.urls import reverse_lazy

from .models import Donation, Institution


class LandingPageView(View):
    def get(self, request, *args, **kwargs):
        donated_bags = Donation.objects.aggregate(Sum('quantity'))
        if donated_bags['quantity__sum'] is None:
            donated_bags['quantity__sum'] = 0
        institutions_supported = Donation.objects.values('institution').distinct().count()
        foundations = Institution.objects.filter(type__exact=1)
        organizations = Institution.objects.filter(type__exact=2)
        local_orgs = Institution.objects.filter(type__exact=3)
        ctx = {
            'donated_bags': donated_bags['quantity__sum'],
            'institutions_supported': institutions_supported,
            'foundations': foundations,
            'organizations': organizations,
            'local_orgs': local_orgs,
        }
        return render(request, 'index.html', ctx)


class AddDonationView(TemplateView):
    template_name = 'form.html'


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'login.html')

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(
            email=email,
            password=password,
        )
        if user is not None:
            login(self.request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'register.html')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'register.html')

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password != password2:
            return HttpResponse('Two different passwords provided! Enter the same password twice.')  # TODO: Proper error.
        user = get_user_model().objects.create_user(
            username=name + surname,
            first_name=name,
            last_name=surname,
            email=email,
            password=password,
        )
        return redirect(reverse_lazy('login'))


class ConfirmationView(TemplateView):
    template_name = 'form-confirmation.html'


class LogoutUserView(LogoutView):
    template_name = 'index.html'

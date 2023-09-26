# account/views.py

from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic.detail import DetailView
# from django.contrib.auth import get_user_model
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import LoginForm, SignupForm

class LoginView(View):
    template_name = 'account/login.html'

    def get(self, request):
        form = LoginForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = LoginForm(request, request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the home page after successful login
        # Handle invalid login
        return render(request, self.template_name, {'form': form})

class SignupView(View):
    template_name = 'account/login.html'

    def get(self, request):
        form = SignupForm()
        return render(request, self.template_name, {'form': form, "signup_page":True})

    def post(self, request):
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful signup
        return render(request, self.template_name, {'form': form})

# class AccountView(DetailView):
#     template_name = 'account/account.html'
#     model = get_user_model()
#     context_object_name = 'user'

class AccountInfoView(LoginRequiredMixin, TemplateView):
    template_name = 'account/account.html'
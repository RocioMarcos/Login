from django.shortcuts import redirect, render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.



class home(LoginRequiredMixin,TemplateView):
    template_name='home.html'
    login_url = reverse_lazy('login')

    
class LoginFormView(FormView):
    template_name='login.html'
    success_url=reverse_lazy('home')
    form_class=AuthenticationForm

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        messages.success(self.request, "Has iniciado session exitosamente")
        return HttpResponseRedirect(self.success_url)

# Cerrar Sesion
@login_required(login_url='/iniciarSesion/')
def CerrarSession(request):
    logout(request)
    return redirect('index')
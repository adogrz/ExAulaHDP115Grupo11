from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .models import CanastaBasicaAnual, CanastaBasicaMensual

# Create your views here.


def obtener_lista_canasta_basica(request):
    canastas_basicas_anuales = CanastaBasicaAnual.objects.all()

    return render(request, 'precio_anual.html', {
        'canastas_basicas_anuales': canastas_basicas_anuales
    })


def obtener_canasta_basica(request, canasta_basica_anual_id):
    canasta_basica_anual = get_object_or_404(
        CanastaBasicaAnual, pk=canasta_basica_anual_id)
    canastas_basicas_mensuales = CanastaBasicaMensual.objects.filter(
        anual_id=canasta_basica_anual_id)

    if not canastas_basicas_mensuales:
        return get_object_or_404(CanastaBasicaMensual, anual_id=canasta_basica_anual_id)

    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

    return render(request, 'mensual.html', {
        'canasta_basica_anual': canasta_basica_anual,
        'canastas_basicas_mensuales': canastas_basicas_mensuales,
        'meses': meses
    })


def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('precio_anual')
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error': 'Passwords do not match'
        })


def signout(request):
    logout(request)
    return redirect('precio_anual')


def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password did not match'
            })
        else:
            login(request, user)
            return redirect('precio_anual')

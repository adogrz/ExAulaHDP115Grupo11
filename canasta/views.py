from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import CanastaBasicaMensualForm
from .models import CanastaBasicaAnual, CanastaBasicaMensual
from django.contrib.auth.decorators import login_required, user_passes_test


# Create your views here.


def obtener_lista_canasta_basica(request):
    canastas_basicas_anuales = CanastaBasicaAnual.objects.all()

    return render(request, 'precio_anual.html', {
        'canastas_basicas_anuales': canastas_basicas_anuales
    })


def obtener_canasta_basica(request, canasta_basica_anual_id):
    canasta_basica_anual = get_object_or_404(CanastaBasicaAnual,
                                             pk=canasta_basica_anual_id)
    canastas_basicas_mensuales = CanastaBasicaMensual.objects.filter(
        anual_id=canasta_basica_anual_id)

    if not canastas_basicas_mensuales:
        return get_object_or_404(CanastaBasicaMensual,
                                 anual_id=canasta_basica_anual_id)

    meses = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio',
             'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre',
             'Diciembre']

    return render(request, 'mensual.html', {
        'canasta_basica_anual': canasta_basica_anual,
        'canastas_basicas_mensuales': canastas_basicas_mensuales,
        'meses': meses
    })


@login_required
@user_passes_test(lambda u: u.is_superuser)
def mensual_detail(request, canasta_basica_anual_id, mes_id):
    if request.method == 'GET':
        canasta_basica_mensual = get_object_or_404(CanastaBasicaMensual,
                                                   anual_id=canasta_basica_anual_id,
                                                   id=mes_id)
        form = CanastaBasicaMensualForm(instance=canasta_basica_mensual)

        return render(request, 'mensual_detail.html', {
            'canasta_basica_mensual': canasta_basica_mensual,
            'form': form
        })
    else:
        canasta_basica_mensual = get_object_or_404(CanastaBasicaMensual,
                                                   anual_id=canasta_basica_anual_id,
                                                   id=mes_id)
        form = CanastaBasicaMensualForm(request.POST,
                                        instance=canasta_basica_mensual)
        form.save()
        canasta_basica_anual = get_object_or_404(CanastaBasicaAnual,
                                                 pk=canasta_basica_anual_id)
        canastas_basicas_mensuales = CanastaBasicaMensual.objects.filter(
            anual_id=canasta_basica_anual_id)

        if not canastas_basicas_mensuales:
            return get_object_or_404(CanastaBasicaMensual,
                                     anual_id=canasta_basica_anual_id)

        precio_promedio = sum(
            [canasta_basica_mensual.precio for canasta_basica_mensual in
             canastas_basicas_mensuales]) / len(canastas_basicas_mensuales)

        canasta_basica_anual.precio_promedio = precio_promedio
        canasta_basica_anual.save()

        canastas_basicas_anuales = CanastaBasicaAnual.objects.all()
        for i, canasta_basica_anual in enumerate(canastas_basicas_anuales):
            if i > 0:
                precio_actual = canasta_basica_anual.precio_promedio
                precio_anterior = canastas_basicas_anuales[
                    i - 1].precio_promedio
                if i != 0:
                    inflacion = ((
                                         precio_actual - precio_anterior) / precio_anterior) * 100
                    canasta_basica_anual.inflacion = inflacion
                canasta_basica_anual.save()

        return redirect('mensual',
                        canasta_basica_anual_id=canasta_basica_anual_id)


def signup(request):
    template_name = 'signup.html'

    if request.method == 'GET':
        return render(request, template_name, {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(
                    username=request.POST['username'],
                    password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('precio_anual')
            except IntegrityError:
                return render(request, template_name, {
                    'form': UserCreationForm,
                    'error': 'Username already exists'
                })
        return render(request, template_name, {
            'form': UserCreationForm,
            'error': 'Passwords do not match'
        })


@login_required
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
            request, username=request.POST['username'],
            password=request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error': 'Username or password did not match'
            })
        else:
            login(request, user)
            return redirect('precio_anual')

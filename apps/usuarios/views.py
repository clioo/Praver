from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from apps.usuarios.forms import LoginForm,RegistrarAgenteForm,RegistrarForm
from django.contrib.auth.decorators import login_required

from apps.inmueble.models import ImagenesInmbueble,Inmueble
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/login/')
def vista_logout(request):
    logout(request)
    return redirect('index')

def vista_login(request):
    form  = LoginForm(request.POST or None)
    context = {"form":form}
    if request.user.is_authenticated():
        return redirect('index')
    if form.is_valid():
        username= form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('index')
    return render(request,"usuarios/login.html",context)

def vista_registrarAgente(request):
    if request.user.is_authenticated():
        return redirect('index')
    if request.method == 'POST':
        form = RegistrarForm(request.POST)
        profile_form = RegistrarAgenteForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user  = form.save(commit=False)
            password = form.cleaned_data.get('password')
            user.set_password(password)
            user.save()
            new_user = authenticate(username=user.username,password=password)
            login(request,new_user)
            profile_form = RegistrarAgenteForm(request.POST, instance=request.user.profile)
            profile_form.save()
            messages.success(request,"Felicidades "+str(user.username)+", bienvenido")
            return redirect('index')
    else:
        form = RegistrarForm()
        profile_form = RegistrarAgenteForm()
    context = {
    "form":form,
    "profile_form": profile_form
    }
    return render(request, "usuarios/registrarAgente.html", context)

def vista_regex(request):
    inmueble = Inmueble.objects.last()
    imagenes = ImagenesInmbueble.objects.filter(inmueble=inmueble.id)
    return render(request,'regEx/regEx.html',{'imagenes':imagenes})
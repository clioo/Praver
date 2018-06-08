from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from apps.usuarios.forms import LoginForm,RegistrarAgenteForm,RegistrarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.inmueble.models import ImagenesInmbueble,Inmueble
from apps.usuarios.models import Profile
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
        username= str(form.cleaned_data.get('username')).lower()
        print(username)
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect('index')
    return render(request,"usuarios/login.html",context)

def vista_registrar(request):
    if request.user.is_authenticated():
        return redirect('index')
    if request.method == 'POST':
        form = RegistrarForm(request.POST or None)
        user  = form.save(commit=False)
        user.email = str(request.POST.get('correo')).lower()
        user.username = str(request.POST.get('correo')).lower()
        password = request.POST.get('contrasena')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=str(request.POST.get('correo')).lower(),password=password)
        login(request,new_user)
        profile_form = Profile.objects.get(user=request.user)
        profile_form.nombre = request.POST.get('nombre')
        profile_form.apellidoPaterno =  request.POST.get('apellido_paterno')
        profile_form.apellidoMaterno = request.POST.get('apellido_materno')
        profile_form.telefono =  request.POST.get('telefono1')
        profile_form.telefono2 = request.POST.get('telefono2')
        profile_form.save()
        return redirect('index')
    else:
        form = RegistrarForm()
        profile_form = RegistrarAgenteForm()
    context = {
    "form":form,
    "profile_form": profile_form
    }
    return render(request, "usuarios/registrar.html", context)

def vista_json_correoDisponible(request):
    correo = request.GET.get('correo',None)
    if User.objects.filter(email=correo):
        return HttpResponse("False")
    return HttpResponse("True")

def vista_regex(request):
    return render(request,'regEx/regEx.html')
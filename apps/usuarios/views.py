from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from apps.usuarios.forms import LoginForm,RegistrarAgenteForm,RegistrarForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from apps.inmueble.models import ImagenesInmbueble,Inmueble
from apps.usuarios.models import Profile
from apps.inmueble.serializers import *
# Create your views here.

def vista_ajax_autenticar(request):
    contrasena = request.GET.get('contrasena',None)
    usuario = authenticate(username=request.user.username,password=contrasena)
    if usuario:
        return HttpResponse("True")
        pass
    return HttpResponse("False")

@login_required(login_url='/login/')
def vista_updateProfile(request):
    prueba = User.objects.get(id=request.user.id)
    if request.method == "POST":
        perfil = Profile.objects.get(user=request.user.id)

        archivo = request.FILES.get('imagen') 
        if archivo:
            perfil.foto = archivo
            perfil.save()
            messages.success(request,"Foto actualizada con éxito")
            pass
        if request.POST.get("correo"):
            user = User.objects.get(id=request.user.id)
            user.username = request.POST.get("correo")
            user.email = request.POST.get("correo")
            user.save()
            messages.success(request,"Correo actualizado con éxito")
            pass
        if request.POST.get("contrasenaNueva"):
            user = User.objects.get(id=request.user.id)
            user.set_password(request.POST.get("contrasenaNueva"))
            user.save()
            user = authenticate(username=user.username,password=request.POST.get("contrasenaNueva"))
            login(request,user)
            messages.success(request,"Contraseña actualizada con éxito")
            pass
        return redirect("actualizarPerfil")
        
        
        pass
    return render(request,"usuarios/perfil.html")
    
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
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        login(request,user)
        return redirect(request.path)
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
        messages.success(request,"¡Bienvenidx " + request.POST.get('nombre') + "! aquí puedes actualizar tu foto de perfil si lo deseas.")
        return redirect('actualizarPerfil')
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
    correo = str(correo).lower()
    if User.objects.filter(email=correo):
        return HttpResponse("False")
    return HttpResponse("True")

def vista_regex(request):
    return render(request,'regEx/regEx.html')

@login_required(login_url='/login/')
def vista_tus_inmuebles(request):
    inmuebles = Inmueble.objects.filter(user=request.user)
    serializer = InmuebleSerializer(inmuebles,many=True)
    print(inmuebles)
    labels = []
    contador = []
    for inmueble in inmuebles:
        labels.append(inmueble.id)
        contador.append(inmueble.contadorVisitas)
        print(inmueble.id)
        pass
    return render(request,"inmueble/anuncios.html",{'inmuebles':serializer.data,'labels':labels,'contador':contador})


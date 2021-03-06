from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.inmueble.serializers import InmuebleSerializer,ImagenesInmbuebleSerializer,LocalidadesSerializer
from django.shortcuts import render,redirect
from django.db.models import Count
from apps.inmueble.forms import InmuebleForm,ImagenesForm
from apps.inmueble.models import Localidades,Inmueble,ImagenesInmbueble
from django.http import JsonResponse,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from django.db.models import Q #esta funcion hace queries por 
from decimal import Decimal
from django.contrib import messages
# Create your views here.
@login_required(login_url='/login/')
def vistaPublicar(request):
    form = InmuebleForm(request.POST or None)
    if request.method == 'POST':
        datos = form.save(commit=False)
        datos.titulo = request.POST.get('titulo')
        datos.descripcion = request.POST.get('descripcion')
        datos.tipoInmueble = request.POST.get('tipoInmueble')
        datos.antiguedad = request.POST.get('antiguedad')
        datos.recamaras = request.POST.get('recamaras')
        datos.estacionamiento= request.POST.get('estacionamiento')
        datos.banos  = request.POST.get('banos')
        datos.mediosBanos= request.POST.get('mediosBanos')
        if request.POST.get('tipoVenta') is not None:
            datos.precioVenta = request.POST.get('precioVenta')
            datos.tipoVenta = True
            pass
        if request.POST.get('tipoRenta') is not None:
            datos.precioRenta = request.POST.get('precioRenta')
            datos.tipoRenta = True
        if request.POST.get('tipoTraspaso'):
            datos.precioTraspaso = request.POST.get('precioTraspaso')
            datos.tipoTraspaso = True
            pass
        datos.metrosConstruidos = request.POST.get('metrosConstruidos')
        datos.metrosTotales = request.POST.get('metrosTotales')
        datos.entidad = request.POST.get('entidad')
        datos.municipio = request.POST.get('municipio')
        datos.colonia = request.POST.get('colonia')
        datos.calle = request.POST.get('calle')
        datos.numExt = request.POST.get('numExt')
        datos.numInt = request.POST.get('numInt')
        datos.codigoPostal = request.POST.get('codigoPostal')
        datos.mostrarMapa = request.POST.get('mostrarMapa')
        datos.latitud = request.POST.get('latitud')
        datos.longitud = request.POST.get('longitud')
        if request.POST.get('servicioAire'):
            datos.servicioAire = request.POST.get('servicioAire')
        if request.POST.get('servicioGas'):
            datos.servicioGas = request.POST.get('servicioGas')
            pass
        if request.POST.get('servicioSegu'):
            datos.servicioSegu = request.POST.get('servicioSegu')
            pass
        if request.POST.get('servicioCale'):
            datos.servicioCale = request.POST.get('servicioCale')
            pass
        if request.POST.get('servicioAmu'):
            datos.servicioAmu = request.POST.get('servicioAmu')
            pass
        if request.POST.get('estadoConservacion'):
            datos.estadoConservacion = request.POST.get('estadoConservacion')
            pass
        datos.avisoDestacado = False
        datos.user = request.user
        datos.save()

        imagenes = request.FILES.getlist('archivos')
        for imagen in imagenes:
            inmueble = Inmueble.objects.last()
            ImagenesInmbueble.objects.create(inmueble=inmueble,imagen=imagen)
            pass
        messages.success(request,"¡Tu inmueble ha sido publicado! Puedes encontrarlo aquí, la sección de tus anuncios.")
        return redirect("tusInmuebles")
    estados = Localidades.objects.values('c_estado','d_estado').annotate(Count('d_estado'))
    estados = estados.order_by('d_estado')
    return render(request,"inmueble/publicar.html",{'form':form, 'estados':estados})
    pass

def ajax_getMunicipios(request):
    c_estado = request.GET.get('estado',None)
    municipios = Localidades.objects.values('D_mnpio','c_mnpio').annotate(Count('D_mnpio'))
    municipios = municipios.filter(c_estado=c_estado)
    municipios = municipios.order_by('D_mnpio')
    descripcion = []
    clave = []
    for municipio in municipios:
        descripcion.append(municipio['D_mnpio'])
        clave.append(municipio['c_mnpio'])
        pass
    arreglo = []
    arreglo.append(descripcion)
    arreglo.append(clave)
    return JsonResponse(arreglo,safe=False)
    pass

def ajax_getColonias(request):
    c_municipio = request.GET.get('municipio',None)
    c_estado = request.GET.get('estado',None)
    colonias = Localidades.objects.filter(c_mnpio=c_municipio,c_estado=c_estado)
    colonias = colonias.order_by('d_asenta')
    serializer  = LocalidadesSerializer(colonias,many=True)
    return JsonResponse(serializer.data,safe=False)
    pass

def ajax_contadorVisitas(request,id_inmueble):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    inmueble.contadorVisitas = inmueble.contadorVisitas + 1
    inmueble.save()
    return HttpResponse("")

@api_view(['GET'])
def vista_json_mapaInmuebles(request,lat1,lat2,lon1,lon2): #,lat1,lat2,lon1,lon2
    inmuebles = Inmueble.objects.filter(longitud__gt=lon2
    ).filter(longitud__lte=lon1
    ).filter(latitud__gt=lat2
    ).filter(latitud__lte=lat1)#longitud2,longitud1,latitud2,latitud1
    serializer = InmuebleSerializer(inmuebles,many=True)
    if serializer.data:
        return JsonResponse(serializer.data,safe=False)
    return HttpResponse("Error")
    pass
def vista_json_latLonInmueble(request,lat,lon): #,lat1,lat2,lon1,lon2
    print(Inmueble.objects.last().latitud)
    print(Inmueble.objects.last().longitud)
    inmuebles = Inmueble.objects.filter(latitud=lat).filter(longitud=lon)
    serializer = InmuebleSerializer(inmuebles,many=True)
    if serializer.data:
        return JsonResponse(serializer.data,safe=False)
    return HttpResponse("Error")
    pass
def vista_json_imagenesInmueble(request,idInmueble):
    imagenes = ImagenesInmbueble.objects.filter(inmueble=idInmueble)
    serializer = ImagenesInmbuebleSerializer(imagenes,many=True)
    if serializer.data:
        return JsonResponse(serializer.data,safe=False)
    return HttpResponse("Error")
    pass

def vista_inmueble_individual(request,id_inmueble):
    inmueble = Inmueble.objects.filter(id=id_inmueble)
    serializer = InmuebleSerializer(inmueble,many=True)
    if serializer.data:
        return render(request,"inmueble/inmuebleIndividual.html",context={'inmuebles':serializer.data})
        pass
    else:
        return HttpResponse("Error")
    
'''tipoInmueble="-",recamaras="-",estacionamiento="-",
banos="-",mediosBanos="-",tipoVenta="-",tipoRenta="-",
tipoTraspaso="-",precioVenta="-",precioRenta="-",precioTraspaso="-",
entidad,municipio,colonia="-",
servicioGas="-",servicioAire="-",servicioSegu="-",servicioCale="-",servicioAmu="-"'''
def vista_lista_inmuebles(request,cadenaBusqueda,tipoVenta):
    cadenas = cadenaBusqueda.split(",")
    consulta = Q()
    for cadena in cadenas:
        consulta |= Q(D_mnpio__icontains=cadena)
        consulta |= Q(d_ciudad__icontains=cadena)
        consulta |= Q(d_asenta__icontains=cadena)
        consulta |= Q(d_estado__icontains=cadena)
        pass
    localidades =Localidades.objects.filter(consulta)
    consulta2 = Q()
    makesFilter = False #verifica si se aplica algún filtro para no sacar nada
    for localidad in localidades:
        makesFilter = True
        consulta2 |= Q(codigoPostal=localidad.d_codigo)
    
    if makesFilter:
        inmuebles = Inmueble.objects.filter(consulta2)
        if tipoVenta:
            tipoVenta = tipoVenta.split(",")
            for tipo in tipoVenta:
                if tipo == "c":
                    inmuebles = inmuebles.filter(tipoVenta=True)
                    pass
                if tipo == "r":
                    inmuebles = inmuebles.filter(tipoRenta=True)
                    pass
                if tipo == "t":
                    inmuebles = inmuebles.filter(tipoTraspaso=True)
                    pass
                pass
        pass
        
    serializer = InmuebleSerializer(inmuebles,many=True)
    return render(request,"inmueble/lista-inmuebles.html",{'inmuebles':serializer.data})
    pass
def vista_json_filtroInmuebles(request,lat1,lat2,lon1,lon2,precioMin="-",precioMax="-",tipoInmueble="-",recamaras="-",estacionamiento="-",banos="-",mediosBanos="-",tipoVenta="-",tipoRenta="-",tipoTraspaso="-",servicioGas="-",servicioAire="-",servicioSegu="-",servicioCale="-",servicioAmu="-"):
    #tendré que hacer una api donde manden cadena de caracteres y yo les devuelva la entidad, municipio y colonia
    query = Q()
    if tipoInmueble != "-":
        query &= Q(tipoInmueble=tipoInmueble)
    if recamaras != "-":
        query &= Q(recamaras="5")
    if estacionamiento != "-":
        query &= Q(estacionamiento=estacionamiento)
    if banos != "-":
        query &= Q(banos=banos)
    if mediosBanos != "-":
        query &= Q(mediosBanos=mediosBanos)
    if tipoVenta != "-":
         query &= Q(tipoVenta=True)
         if precioMin != "-" and precioMax != "-":
            query &= Q(precioVenta__gt=precioMin)
            query &= Q(precioVenta__lte=precioMax)
    if tipoRenta != "-":
        query &= Q(tipoRenta=True)
        if precioMin != "-" and precioMax != "-":
            query &= Q(precioRenta__gt=precioMin)
            query &= Q(precioRenta__lte=precioMax)
    if tipoTraspaso != "-":
        query &= Q(tipoTraspaso=True)
        if precioMin != "-" and precioMax != "-":
            query &= Q(precioTraspaso__gt=precioMin)
            query &= Q(precioTraspaso__lte=precioMax)
    if servicioGas != "-":
        query &= Q(servicioGas=True)
    if servicioAire != "-":
        query &= Q(servicioAire=True)
    if servicioSegu != "-":
        query &= Q(servicioSegu=True)
    if servicioCale != "-":
        query &= Q(servicioCale=True)
    if servicioAmu != "-":
        query &= Q(servicioAmu=True)
    # PENDIENTE RANGO DE PRECIOS query &= Q(precioVenta)query &= Q(precioRenta)query &= Q(precioTraspaso)
    inmuebles = Inmueble.objects.filter(longitud__gt=lon2
    ).filter(longitud__lte=lon1
    ).filter(latitud__gt=lat2
    ).filter(latitud__lte=lat1).filter(query)#longitud2,longitud1,latitud2,latitud1
    serializer = InmuebleSerializer(inmuebles,many=True)
    if serializer.data:
        return JsonResponse(serializer.data,safe=False)
    return HttpResponse("Error")

@login_required(login_url='/login/')
def vista_eliminarInmueble(request,id_inmueble):
    inmueble = Inmueble.objects.filter(id=id_inmueble)
    inmueble.delete()
    return redirect('tusInmuebles')

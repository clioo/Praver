from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from apps.inmueble.serializers import InmuebleSerializer,ImagenesInmbuebleSerializer
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
    colonias = Localidades.objects.values('d_asenta','d_codigo')
    colonias = colonias.filter(c_mnpio=c_municipio,c_estado=c_estado)
    colonias = colonias.order_by('d_asenta')
    descripcion = []
    clave = []
    for colonia in colonias:
        descripcion.append(colonia['d_asenta'])
        clave.append(colonia['d_codigo'])
        pass
    arreglo = []
    arreglo.append(descripcion)
    arreglo.append(clave)

    return JsonResponse(arreglo,safe=False)
    pass

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

#tipoInmueble="-",recamaras="-",estacionamiento="-",banos="-",mediosBanos="-",tipoVenta="-",tipoRenta="-",tipoTraspaso="-",precioVenta="-",precioRenta="-",precioTraspaso="-",metrosConstruidos="-",metrosTotales="-",entidad,municipio,colonia="-",servicioGas="-",servicioAire="-",servicioSegu="-",servicioCale="-",servicioAmu="-"
def vista_json_filtroInmuebles(request):
    query = Q()
    query &= Q(tipoInmueble='casa')
    query &= Q(recamaras="5")
    inmuebles = Inmueble.objects.filter(query)
    serializer = InmuebleSerializer(inmuebles,many=True)
    if inmuebles:
        return JsonResponse(serializer.data,safe=False)
    return HttpResponse("Error")
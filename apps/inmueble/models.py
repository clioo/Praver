from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Inmueble(models.Model):
    #Opciones____________________
    opcionesServicios = (('gas',"Gas"),('aire',"Aire acondicionado"),('segu',"Seguridad privada"),('cale',"Calefacción"),('amu',"Amueblada"))
    opcionesEstadoConserva = (('buen',"Bueno"),('malo',"Malo"),('remod', "Para remodelar"),('vand', "Vandalizada"))
    opcionesTipoInmueble = (('casa','Casa'),('depa',"Departamento"),('dupl',"Dúplex"),('ofic',"Oficina"),('loca',"Local comercial"))
    opcionesMostrarMapa = (('exac',"Mostrar ubicación exacta"),('apro',"Mostrar ubicación aproximada"),('no',"No mostrar"))
    #-----------------------------------------------
    user = models.ForeignKey(User)
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=200)
    tipoInmueble = models.CharField(max_length=10,choices=opcionesTipoInmueble)
    antiguedad = models.CharField(max_length=20,blank=True,null=True)
    recamaras = models.CharField(max_length=20)
    estacionamiento = models.CharField(max_length=20)
    banos = models.CharField(max_length=20)
    mediosBanos = models.CharField(max_length=20)
    #Tipo de venta
    tipoVenta = models.BooleanField(default=False)
    tipoRenta = models.BooleanField(default=False)
    tipoTraspaso = models.BooleanField(default=False)
    #_________
    precioVenta = models.CharField(max_length=20,blank=True,null=True)
    precioRenta = models.CharField(max_length=20,blank=True,null=True)
    precioTraspaso = models.CharField(max_length=20,blank=True,null=True)
    metrosConstruidos = models.CharField(max_length=20)
    metrosTotales = models.CharField(max_length=20)
    entidad = models.CharField(max_length=30)
    municipio = models.CharField(max_length=30)
    colonia = models.CharField(max_length=30)
    calle = models.CharField(max_length=30)
    numExt = models.CharField(max_length=4)
    numInt = models.CharField(max_length=5,blank=True,null=True)
    codigoPostal = models.CharField(max_length=30,blank=True,null=True)
    mostrarMapa = models.CharField(max_length=4,choices=opcionesMostrarMapa)
    latitud =  models.CharField(max_length=100,blank=True,null=True)
    longitud = models.CharField(max_length=100,blank=True,null=True)
    #Servicios del inmbuelbe
    servicioGas = models.BooleanField(default=False)
    servicioAire = models.BooleanField(default=False)
    servicioSegu = models.BooleanField(default=False)#Seguridad privada
    sevicioCale = models.BooleanField(default=False) #Calefaccion
    servicioAmu = models.BooleanField(default=False)#Amueblada
    #_____________________
    estadoConservacion = models.CharField(max_length=4, choices=opcionesEstadoConserva)
    avisoDestacado = models.BooleanField(default=False)

class ImagenesInmbueble(models.Model):
    inmueble  = models.ForeignKey(Inmueble)
    imagen =models.ImageField()

class Localidades(models.Model):
    d_codigo = models.CharField(max_length=10)
    d_asenta = models.CharField(max_length=100)
    D_mnpio = models.CharField(max_length=100)
    c_mnpio = models.CharField(max_length=10)
    c_estado = models.CharField(max_length=10)
    d_estado = models.CharField(max_length=50)
    class Meta:
        managed = False
        db_table = 'Localidades'
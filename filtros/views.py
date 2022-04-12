import pandas as pd
from datetime import datetime
from shapely.geometry import Point
from shapely import wkt
import csv

from django.conf import settings
#
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ArchViajes, DatosCsv

from .serializers import (
    ArchViajeSerializer,
    FiltroSemanaSerializer,
    CuadradoSerializer,
    FiltroHoraSerializer,
    FiltroSourceSerializer,
    FiltroRegionSerializer,
)


class ViajesApiView(APIView):
#para cargar la data en la base de datos a partir de darle un CSV
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request, *args, **kwargs):
        base_dir = settings.BASE_DIR
        file_serializer = ArchViajeSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            path = file_serializer.validated_data['file']
            print('uno*****************')
            print(base_dir+'/data/'+str(path))
            with open(base_dir+'/data/'+str(path)) as f:
                print('dos*****************')
                reader = csv.reader(f)  
                print('uno*****************')
                for row in reader:
                    print('uno*****************')
                    _, created = DatosCsv.objects.get_or_create(
                        region=row[0],
                        origin_coord=row[1],
                        destination_coord=row[2],
                        datetime=row[3],
                        datasource=row[4],
                        )

            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class FiltroSemana(APIView):
    #obtiene los viaje sque ocurren en una semana 
    #indicando una fecha en dicha semana    
    
    def post(self,request):
        serializer = FiltroSemanaSerializer(data=request.data)
        serializer.is_valid()
        fecha = serializer.validated_data['fecha']
        data = DatosCsv.objects.all()
        datos = pd.DataFrame(data.values())
        datos.drop(index=datos.index[0],axis=0, inplace=True)

      
        
        datos['datetime']=pd.to_datetime(datos['datetime'])
        aux = datos['datetime'].dt.isocalendar().week
        semana =  datetime.strptime(fecha, '%Y-%m-%d').isocalendar()[1]
        #print(datos[aux==semana])
        
        return Response({'filtro por semana' : datos[aux==semana]})



class FiltroCoordenadas(APIView):
    #obtiene los viaje sque ocurren en una semana 
    #indicando una fecha en dicha semana    
    
    def post(self,request):
        serializer = CuadradoSerializer(data=request.data)
        serializer.is_valid()
        y_up = serializer.validated_data['coor_up']
        y_down = serializer.validated_data['coor_down']
        x_right = serializer.validated_data['coor_right']
        x_left = serializer.validated_data[ 'coor_left']
        columna = serializer.validated_data['columna']
        print('**********************************************')
        print(columna)
        data = DatosCsv.objects.all()
        datos = pd.DataFrame(data.values())
        datos.drop(index=datos.index[0],axis=0, inplace=True)

        coord_y = sorted( [y_up,y_down]) ##ordenando me aseguro que busque dentro de la caja que esta definida
        coord_x = sorted([x_right,x_left])

        datos['origin_coord'] = datos['origin_coord'].apply(wkt.loads)
        datos['destination_coord'] = datos['destination_coord'].apply(wkt.loads)
        
        aux = datos[columna].apply(lambda x : True if coord_x[0] < x.x and x.x < coord_x[1] and coord_y[0] < x.y and x.y < coord_y[1] else False)

        resultado = datos[aux]
        resultado["origin_coord"] = resultado["origin_coord"].astype(str) 
        resultado["destination_coord"] = resultado["destination_coord"].astype(str)


        ### promedia los resultados por semana
        resultado['datetime']=pd.to_datetime(resultado['datetime'])
        aux_sem = resultado['datetime'].dt.week
        semanas = aux_sem.unique()
        suma=0
        for i in semanas:
            suma += aux_sem[aux_sem==i].count()


        return Response({'promedio por semana' : suma/len(semanas) , 'filtro por '+str(columna) : resultado })





class FiltroHora(APIView):
    #obtiene los viajes que ocurren en una hora determinada 
        
    def post(self,request):
        serializer = FiltroHoraSerializer(data=request.data)
        serializer.is_valid()
        hora = serializer.validated_data['hora']
        data = DatosCsv.objects.all()
        datos = pd.DataFrame(data.values())
        datos.drop(index=datos.index[0],axis=0, inplace=True)

      
        ### filtra los datos
        datos['datetime']=pd.to_datetime(datos['datetime'])
        aux = datos['datetime'].dt.hour
        hora =  datetime.strptime(hora, '%H:%M').hour
        resultado = datos[aux==hora]
        #print(datos[aux==semana])

        ### promedia los resultados por semana
        aux_sem = resultado['datetime'].dt.week
        semanas = aux_sem.unique()
        suma=0
        for i in semanas:
            suma += aux_sem[aux_sem==i].count()
                
        return Response({'promedio por semana' : suma/len(semanas) ,'filtro por hora' : resultado})



class FiltroSource(APIView):
    #obtiene los viajes que ocurren en una hora determinada 
        
    def post(self,request):
        serializer = FiltroSourceSerializer(data=request.data)
        serializer.is_valid()
        columna = serializer.validated_data['source']
        data = DatosCsv.objects.all()
        datos = pd.DataFrame(data.values())
        datos.drop(index=datos.index[0],axis=0, inplace=True)

      
        ### filtra los datos
        resultado = datos[datos['datasource']==columna]
        #print(datos[aux==semana])

        ### promedia los resultados por semana
        resultado['datetime']=pd.to_datetime(resultado['datetime'])       
        aux_sem = resultado['datetime'].dt.week
        semanas = aux_sem.unique()
        suma=0
        for i in semanas:
            suma += aux_sem[aux_sem==i].count()
                
        return Response({'promedio por semana' : suma/len(semanas) ,'filtro por fuente' : resultado})


class FiltroRegion(APIView):
    #obtiene los viajes que ocurren en una hora determinada 
        
    def post(self,request):
        serializer = FiltroRegionSerializer(data=request.data)
        serializer.is_valid()
        columna = serializer.validated_data['region']
        data = DatosCsv.objects.all()
        datos = pd.DataFrame(data.values())
        datos.drop(index=datos.index[0],axis=0, inplace=True)

      
        ### filtra los datos
        resultado = datos[datos['region']==columna]
        #print(datos[aux==semana])

        ### promedia los resultados por semana
        resultado['datetime']=pd.to_datetime(resultado['datetime'])       
        aux_sem = resultado['datetime'].dt.week
        semanas = aux_sem.unique()
        suma=0
        for i in semanas:
            suma += aux_sem[aux_sem==i].count()
                
        return Response({'promedio por semana' : suma/len(semanas) ,'filtro por región' : resultado})




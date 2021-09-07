"""
Recordatorio de fechas de calibracion de piranometros
Se realiza script que analice la fecha de vencimiento de la calibracion de 
sensores de radiacion solar
Los pasos que debe cumplir el script son:
    Analizar las fechas de vencimiento de la calibracion
    Contar la cantidad de dias desde el ultimo cambio
    Reportar por correo al equipo tecnico las calibraciones proximas a su vencimiento,
    las calibraciones vencidas, y el timedelta de cada una
"""
import pandas as pd

from datetime import date
from datetime import datetime


# Datos de sensores
calibraciones = {
    'Calibracion_valida_hasta':[date(2020,1,22),date(2020,10,29),date(2020,1,21),date(2020,2,20),date(2019,10,31),date(2020,2,20),date(2020,7,22),date(2020,1,21),date(2019,11,8),date(2020,2,19),date(2020,10,29)] }

estaciones = ['Aparicio Saravia','Baltasar Brum','Bonete','Eulacio','Jose Ignacio','Mc Meekan','Otamendi','Piedra Sola','Rocha','Rosendo Mendoza','Rubio']



# Dataframe con informacion de sensores
Registro_piranometros = pd.DataFrame(calibraciones,index=estaciones)
# fecha de comparacion
today = date.today()

def comparacion_de_fechas():
    global Registro_piranometros, today
    calibraciones_por_vencer(Registro_piranometros,today)
    # calibraciones_por_vencer()
    
    
def calibraciones_por_vencer(sensores,fecha_de_hoy):

    inicio_cambio = 365
    maximo = inicio_cambio*2
    
    estacion = []
    dias_de_utilizacion = []
    Vencida = []
    Periodo_de_cambio = []  
    Dias_vencida = []
    
    for ind in range(0,len(sensores.index)):
        print(ind)
        estacion.append(sensores[sensores.columns[0]][ind])
        dias_de_utilizacion.append(fecha_de_hoy-sensores[sensores.columns[0]][ind])
        Vencida.append(sensores[sensores.columns[0]][ind]>=maximo)
        Periodo_de_cambio.append(sensores[sensores.columns[0]][ind]>=inicio_cambio)
        
    for est in range(0,len(Vencida)):
        if Vencida[est]:
            Dias_vencida.append(fecha_de_hoy-dias_de_utilizacion[est]+)
        
            
            
        
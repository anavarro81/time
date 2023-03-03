from datetime import datetime, date, time, timedelta
import calendar

meses_anyo = [
    "enero", 
    "febrero", 
    "marzo", 
    "abril", 
    "mayo", 
    "junio", 
    "julio", 
    "agosto", 
    "septiembre", 
    "octubre", 
    "noviembre", 
    "diciembre"
]




# Obtener la fecha 
ahora = datetime.now()
print ('Fecha y hora: ', ahora)


print (f'El mes actual es: {meses_anyo[ahora.month-1]}')

# Obtener el mes de la fecha
# Crear Excel con el nombre. 
# ¿Qué pasa si existe? 


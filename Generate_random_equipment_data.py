import random
from faker import Faker
from openpyxl import Workbook
import os

fake = Faker("es_ES")
num_rows = 30

wb = Workbook()
ws = wb.active
ws.append(["Serial_case", "Id_Case", "Serial_monitor", "Id_monitor", "Serial_teclado",
           "Id_teclado", "Serial_mouse", "Id_mouse", "Serial_ups", "Id_ups"])

def generar_serial(longitud_maxima):
    return ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789', k=longitud_maxima))

case_contador = 1
monitor_contador = 1
teclado_contador = 1
mouse_contador = 1
ups_contador = 1

def generar_id(prefix, counter):
    return f"{prefix}-{counter:03}"

for _ in range(num_rows):
    serial_case = generar_serial(10)
    id_case = generar_id("MJGA-CASE", case_contador)
    serial_monitor = generar_serial(10)
    id_monitor = generar_id("MJGA-MONITOR", monitor_contador)
    serial_teclado = generar_serial(10)
    id_teclado = generar_id("MJGA-TECLADO", teclado_contador)
    serial_mouse = generar_serial(10)
    id_mouse = generar_id("MJGA-MOUSE", mouse_contador)
    serial_ups = generar_serial(10)
    id_ups = generar_id("MJGA-UPS", ups_contador)
    
    ws.append([serial_case, id_case, serial_monitor, id_monitor, serial_teclado,
               id_teclado, serial_mouse, id_mouse, serial_ups, id_ups])

    case_contador += 1
    monitor_contador += 1
    teclado_contador += 1
    mouse_contador += 1
    ups_contador += 1

#Guardar el archivo .xlsx
filename = "datos_equipos_mantenimiento.xlsx"
wb.save(filename=filename)

print("Se ha generado el archivo .xlsx")

#Abrir el archivo .xlsx generado
os.startfile(filename)

import random
from faker import Faker
from openpyxl import Workbook
import os

fake = Faker("es_ES")
num_rows = 20

wb = Workbook()
ws = wb.active
ws.append(["ID", "Nombres y Apellidos", "Correo electrónico", "Fecha de Nacimiento", "Profesión"])

for _ in range(num_rows):
    #Generar dos nombres y dos apellidos
    nombres = fake.first_name()
    segundo_nombre = fake.first_name()
    apellidos = fake.last_name()
    segundo_apellido = fake.last_name()
    
    id_aleatorio = "11" + ''.join([str(random.randint(0, 9)) for _ in range(8)])
    
    nombre_completo = f"{nombres} {segundo_nombre} {apellidos} {segundo_apellido}"
    correo = (
        nombres.lower() + "_" + apellidos.lower() + 
        "@"
        + fake.random_element(elements=("gmail.com", "hotmail.com", "outlook.com", "yahoo.com"))
    )
    
    profesion = fake.job()
    fecha_nacimiento = fake.date_of_birth(minimum_age=18, maximum_age=60)
    fecha_nacimiento_str = fecha_nacimiento.strftime("%Y-%m-%d")
    
    #Agregar los datos a la hoja de cálculo
    ws.append([id_aleatorio, nombre_completo, correo, fecha_nacimiento_str, profesion])

#Guardar el archivo .xlsx
filename = "datos_aleatorios.xlsx"
wb.save(filename=filename)

print("Se ha generado el archivo .xlsx")

#Abrir el archivo .xlsx
os.startfile(filename)

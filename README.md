
# Generadores de Datos Aleatorios en Excel

Este repositorio contiene scripts de Python que generan datos aleatorios y los guardan en archivos Excel (.xlsx) utilizando diferentes enfoques.

## Script 1: Generador de Datos Personales

El script `Generate_random_user_data.py` utiliza la biblioteca `Faker` para generar nombres, correos electrónicos, fechas de nacimiento y profesiones aleatorias, y la biblioteca `openpyxl` para almacenar los datos en un archivo Excel.

### Descripción

El script genera una lista de personas con los siguientes campos:
- ID
- Nombres y Apellidos
- Correo Electrónico
- Fecha de Nacimiento
- Profesión

Los datos se almacenan en un archivo Excel llamado `datos_aleatorios.xlsx`

## Script 2: Generador de Equipos de Mantenimiento

El script `Generate_equipment_data.py` genera datos de equipos de mantenimiento con números de serie y IDs únicos para diferentes componentes, y la biblioteca `openpyxl` para almacenar los datos en un archivo Excel.

### Descripción

El script genera datos de equipos con los siguientes campos:

- Serial_case
- Id_Case
- Serial_monitor
- Id_monitor
- Serial_teclado
- Id_teclado
- Serial_mouse
- Id_mouse
- Serial_ups
- Id_ups

Los datos se almacenan en un archivo Excel llamado `datos_equipos_mantenimiento.xlsx`

## Instalación

Para ejecutar los scripts, necesitas instalar las siguientes bibliotecas de Python:

### Faker

```bash
pip install faker 
```
### Openpyxl

```bash
pip install openpyxl
```

## Contribución

Si quieres contribuir a este proyecto, siéntete libre de hacer un `fork` del repositorio y enviar un `pull request` con tus mejoras.


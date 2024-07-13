from cx_Freeze import setup, Executable
import os

actual_path = os.path.dirname(__file__)

main = os.path.join(actual_path,"main.py")

# Nombre del archivo principal (el que contiene la interfaz Tkinter)
main_script = main

# Opciones de configuración
build_options = {
    'packages': ['tkinter'],
    'excludes': [],
}

executables = [
    Executable(main_script, base='Win32GUI', target_name='Terminal_Fallout.exe')
]

setup(
    name='Terminal_Fallout',
    version='1.1',
    description='En: It\'s a solver of Fallout terminal minigame. \n Es: Es un solucionador del minijuego de terminal en Fallout.',
    options={'build_exe': build_options},
    executables=executables
)

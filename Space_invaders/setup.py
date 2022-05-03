import sys
from cx_Freeze import setup, Executable

include_files= ['autorun.inf']
base= None

if sys.platform=="win32":
    base= "Win32GUI"

setup(name="jueguecito",
      version="0.1",
      description= "Juego chachi de ordenador",
      options={'build_exe': {'include_files': include_files}},
      executables=[Executable("main.py",base=base)]) #no hace falta incluir los archivos importados


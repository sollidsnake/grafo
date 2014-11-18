import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(name = "Grafo",
      version = "3.1",
      executables = [Executable("main.py", base=base)]
)

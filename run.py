#!/usr/bin/env python3
"""
Lanzador de la aplicación Presente Histórico
"""
import os
import sys
import subprocess
import platform
from pathlib import Path

def main():
    project_dir = Path(__file__).parent.absolute()
    
    if platform.system() == "Windows":
        python_path = project_dir / "venv" / "Scripts" / "python"
    else:
        python_path = project_dir / "venv" / "bin" / "python"
    
    if not python_path.exists():
        print("❌ Entorno virtual no encontrado. Ejecuta 'python installer.py' primero")
        return 1
    
    os.chdir(project_dir)
    
    # Ejecutar la aplicación
    cmd = [str(python_path), "app.py"]
    
    try:
        subprocess.run(cmd)
    except KeyboardInterrupt:
        print("\n\n👋 Aplicación detenida")
    except Exception as e:
        print(f"❌ Error al ejecutar la aplicación: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())

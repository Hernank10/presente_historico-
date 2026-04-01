#!/usr/bin/env python3
"""
Instalador de la Aplicación Educativa "Presente Histórico"
Este script automatiza la instalación y configuración del proyecto.
"""

import os
import sys
import subprocess
import platform
import shutil
import json
from pathlib import Path

class PresenteHistoricoInstaller:
    """Instalador de la aplicación Presente Histórico"""
    
    def __init__(self):
        self.project_dir = Path(__file__).parent.absolute()
        self.venv_dir = self.project_dir / "venv"
        self.python_cmd = "python3" if platform.system() != "Windows" else "python"
        
    def print_header(self):
        """Imprime el encabezado del instalador"""
        print("=" * 60)
        print("  📚 INSTALADOR - ESTUDIO DEL PRESENTE HISTÓRICO")
        print("=" * 60)
        print(f"  Sistema: {platform.system()} {platform.release()}")
        print(f"  Directorio: {self.project_dir}")
        print("=" * 60)
        print()
    
    def check_python(self):
        """Verifica que Python está instalado y es compatible"""
        print("🔍 Verificando Python...")
        
        try:
            result = subprocess.run(
                [self.python_cmd, "--version"],
                capture_output=True,
                text=True
            )
            version = result.stdout.strip()
            print(f"   ✅ {version}")
            
            # Verificar versión (Python 3.6+)
            version_num = version.split()[1].split(".")
            if int(version_num[0]) < 3 or (int(version_num[0]) == 3 and int(version_num[1]) < 6):
                print("   ⚠️  Se recomienda Python 3.6 o superior")
                
            return True
        except FileNotFoundError:
            print("   ❌ Python no está instalado o no está en el PATH")
            print("   📥 Descarga Python desde: https://www.python.org/downloads/")
            return False
    
    def check_pip(self):
        """Verifica que pip está instalado"""
        print("\n🔍 Verificando pip...")
        
        try:
            result = subprocess.run(
                [self.python_cmd, "-m", "pip", "--version"],
                capture_output=True,
                text=True
            )
            print(f"   ✅ {result.stdout.strip()}")
            return True
        except:
            print("   ❌ pip no está disponible")
            return False
    
    def create_virtualenv(self):
        """Crea el entorno virtual"""
        print("\n🔧 Creando entorno virtual...")
        
        if self.venv_dir.exists():
            print("   ℹ️  El entorno virtual ya existe")
            response = input("   ¿Deseas recrearlo? (s/N): ").lower()
            if response == 's':
                shutil.rmtree(self.venv_dir)
                print("   🗑️  Entorno virtual eliminado")
            else:
                return True
        
        try:
            subprocess.run(
                [self.python_cmd, "-m", "venv", str(self.venv_dir)],
                check=True,
                capture_output=True
            )
            print("   ✅ Entorno virtual creado correctamente")
            return True
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Error al crear entorno virtual: {e}")
            return False
    
    def get_pip_path(self):
        """Obtiene la ruta del pip dentro del entorno virtual"""
        if platform.system() == "Windows":
            return self.venv_dir / "Scripts" / "pip"
        else:
            return self.venv_dir / "bin" / "pip"
    
    def install_dependencies(self):
        """Instala las dependencias desde requirements.txt"""
        print("\n📦 Instalando dependencias...")
        
        pip_path = self.get_pip_path()
        req_file = self.project_dir / "requirements.txt"
        
        if not req_file.exists():
            print("   ⚠️  No se encontró requirements.txt")
            self.create_requirements()
        
        try:
            subprocess.run(
                [str(pip_path), "install", "-r", str(req_file)],
                check=True,
                capture_output=False
            )
            print("   ✅ Dependencias instaladas correctamente")
            return True
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Error al instalar dependencias: {e}")
            return False
    
    def create_requirements(self):
        """Crea el archivo requirements.txt si no existe"""
        print("\n📝 Creando requirements.txt...")
        
        requirements = [
            "Flask==2.3.2",
            "Flask-SQLAlchemy==3.0.5",
            "Flask-CORS==4.0.0",
            "SQLAlchemy==2.0.48"
        ]
        
        req_file = self.project_dir / "requirements.txt"
        with open(req_file, "w") as f:
            f.write("\n".join(requirements))
        
        print("   ✅ requirements.txt creado")
    
    def create_data_files(self):
        """Crea los archivos de datos si no existen"""
        print("\n📁 Creando archivos de datos...")
        
        data_dir = self.project_dir / "data"
        data_dir.mkdir(exist_ok=True)
        
        # Crear estudiantes.json si no existe
        estudiantes_file = data_dir / "estudiantes.json"
        if not estudiantes_file.exists():
            with open(estudiantes_file, "w") as f:
                json.dump({"estudiantes": []}, f, indent=2)
            print("   ✅ estudiantes.json creado")
        
        # Crear usuarios.json si no existe
        usuarios_file = data_dir / "usuarios.json"
        if not usuarios_file.exists():
            with open(usuarios_file, "w") as f:
                json.dump({
                    "usuarios": [
                        {
                            "id": 1,
                            "username": "admin",
                            "password": "admin123",
                            "rol": "administrador",
                            "email": "admin@ejemplo.com",
                            "fecha_creacion": "2024-01-01"
                        }
                    ]
                }, f, indent=2)
            print("   ✅ usuarios.json creado con usuario admin")
        
        # Crear ejercicios.json si no existe
        ejercicios_file = data_dir / "ejercicios.json"
        if not ejercicios_file.exists():
            print("   ⚠️  ejercicios.json no encontrado - se generará al ejecutar la app")
        
        # Crear flashcards.json si no existe
        flashcards_file = data_dir / "flashcards.json"
        if not flashcards_file.exists():
            print("   ⚠️  flashcards.json no encontrado - se generará al ejecutar la app")
    
    def create_launcher(self):
        """Crea el script de lanzamiento"""
        print("\n🚀 Creando lanzador...")
        
        launcher_path = self.project_dir / "run.py"
        
        launcher_content = '''#!/usr/bin/env python3
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
        print("\\n\\n👋 Aplicación detenida")
    except Exception as e:
        print(f"❌ Error al ejecutar la aplicación: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
'''
        
        with open(launcher_path, "w") as f:
            f.write(launcher_content)
        
        # Hacer ejecutable en Unix
        if platform.system() != "Windows":
            os.chmod(launcher_path, 0o755)
        
        print("   ✅ Lanzador creado: run.py")
        print("   📌 Para ejecutar la app: python run.py")
    
    def create_quick_install(self):
        """Crea un script de instalación rápida"""
        print("\n⚡ Creando script de instalación rápida...")
        
        if platform.system() == "Windows":
            quick_install = self.project_dir / "install.bat"
            content = '''@echo off
echo ========================================
echo  Instalador Rapido - Presente Historico
echo ========================================
echo.
echo Creando entorno virtual...
python -m venv venv
echo.
echo Instalando dependencias...
call venv\\Scripts\\pip install -r requirements.txt
echo.
echo Instalacion completada!
echo Para ejecutar: run.py
pause
'''
        else:
            quick_install = self.project_dir / "install.sh"
            content = '''#!/bin/bash
echo "========================================"
echo " Instalador Rapido - Presente Historico"
echo "========================================"
echo
echo "Creando entorno virtual..."
python3 -m venv venv
echo
echo "Instalando dependencias..."
source venv/bin/activate
pip install -r requirements.txt
echo
echo "Instalacion completada!"
echo "Para ejecutar: python run.py"
'''
            os.chmod(quick_install, 0o755)
        
        with open(quick_install, "w") as f:
            f.write(content)
        
        print(f"   ✅ Script de instalación rápida creado: {quick_install.name}")
    
    def show_instructions(self):
        """Muestra instrucciones de uso"""
        print("\n" + "=" * 60)
        print("  ✅ INSTALACIÓN COMPLETADA")
        print("=" * 60)
        print()
        print("📌 Para ejecutar la aplicación:")
        print()
        print("   Opción 1 (Recomendada):")
        print("   python run.py")
        print()
        print("   Opción 2 (Activando entorno manual):")
        print("   source venv/bin/activate  # En Windows: venv\\Scripts\\activate")
        print("   python app.py")
        print()
        print("🌐 Acceso a la aplicación:")
        print("   http://localhost:5001")
        print()
        print("🔐 Credenciales administrador:")
        print("   Usuario: admin")
        print("   Contraseña: admin123")
        print()
        print("💡 Consejos:")
        print("   - El progreso se guarda automáticamente en el navegador")
        print("   - Los usuarios se guardan en data/estudiantes.json")
        print("   - Presiona Ctrl+C para detener el servidor")
        print()
        print("=" * 60)
    
    def run(self):
        """Ejecuta el instalador completo"""
        self.print_header()
        
        # Verificar requisitos
        if not self.check_python():
            print("\n❌ Instalación cancelada: Python no está disponible")
            return False
        
        if not self.check_pip():
            print("\n⚠️  Continuando sin pip...")
        
        # Instalar
        if not self.create_virtualenv():
            return False
        
        if not self.install_dependencies():
            print("\n⚠️  Algunas dependencias no se instalaron correctamente")
        
        # Configurar
        self.create_data_files()
        self.create_launcher()
        self.create_quick_install()
        
        # Instrucciones finales
        self.show_instructions()
        
        return True

def main():
    """Función principal"""
    installer = PresenteHistoricoInstaller()
    success = installer.run()
    
    if not success:
        print("\n❌ La instalación no se completó correctamente")
        sys.exit(1)
    else:
        sys.exit(0)

if __name__ == "__main__":
    main()

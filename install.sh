#!/bin/bash
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

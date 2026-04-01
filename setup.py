"""
Setup.py para distribución del paquete Presente Histórico
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="presente-historico",
    version="1.0.0",
    author="Tu Nombre",
    author_email="tu-email@ejemplo.com",
    description="Aplicación educativa para aprender el presente histórico en español",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tu-usuario/presente-historico",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Topic :: Education :: Computer Aided Instruction (CAI)",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    include_package_data=True,
    package_data={
        "presente_historico": [
            "templates/*.html",
            "templates/auth/*.html",
            "templates/admin/*.html",
            "static/css/*.css",
            "static/js/*.js",
            "data/*.json",
        ],
    },
    entry_points={
        "console_scripts": [
            "presente-historico=run:main",
        ],
    },
)

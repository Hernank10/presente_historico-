# 📚 Estudio del Presente Histórico

Aplicación web educativa interactiva para aprender y practicar el uso del presente histórico en español.

## 🎯 Características

- **📖 Teoría Completa**: Explicaciones detalladas con ejemplos
- **🔍 Clasificador Automático**: Analiza textos y clasifica tipos de presente verbal
- **✍️ Reescribidor**: Convierte textos entre pasado/futuro y presente histórico
- **📝 100 Ejercicios**: Organizados por categorías con seguimiento de progreso
- **🃏 50 Flashcards**: Tarjetas interactivas para memorizar conceptos
- **📊 Dashboard Personal**: Seguimiento de progreso, logros y rachas
- **👥 Sistema de Usuarios**: Registro, login y perfil personalizado
- **🔐 Panel Admin**: Gestión de ejercicios y contenido

## 🚀 Tecnologías

- **Backend**: Flask (Python)
- **Frontend**: Bootstrap 5, HTML5, CSS3, JavaScript
- **Base de Datos**: SQLite (Flask-SQLAlchemy)
- **Gráficos**: Chart.js

## 📁 Estructura del Proyecto
## 📁 Estructura del Proyecto
presente_historico/
├── app.py # Aplicación principal Flask
├── requirements.txt # Dependencias Python
├── data/
│ ├── ejercicios.json # 100 ejercicios organizados
│ ├── flashcards.json # 50 flashcards de estudio
│ ├── estudiantes.json # Datos de usuarios registrados
│ └── usuarios.json # Usuarios administradores
├── static/
│ ├── css/
│ │ ├── base.css # Estilos base y variables
│ │ ├── navbar.css # Estilos de navegación
│ │ ├── hero.css # Estilos de sección hero
│ │ ├── cards.css # Estilos de tarjetas
│ │ ├── flashcards.css # Estilos de flashcards
│ │ ├── ejercicios.css # Estilos de ejercicios
│ │ ├── dashboard.css # Estilos de dashboard
│ │ └── admin.css # Estilos de panel admin
│ └── js/
│ └── script.js # Funciones JavaScript globales
├── templates/
│ ├── base.html # Plantilla base
│ ├── index.html # Página principal
│ ├── teoria.html # Teoría del presente histórico
│ ├── clasificador.html # Clasificador de textos
│ ├── reescritor.html # Reescribidor de tiempos
│ ├── practica.html # Práctica con ejemplos
│ ├── ejercicios.html # 100 ejercicios interactivos
│ ├── flashcards.html # Flashcards de estudio
│ ├── dashboard.html # Dashboard de estudiante
│ ├── auth/
│ │ ├── login.html # Inicio de sesión
│ │ ├── registro.html # Registro de usuarios
│ │ └── perfil.html # Perfil de usuario
│ └── admin/
│ ├── login.html # Login administrador
│ ├── dashboard_admin.html
│ ├── ejercicios_admin.html
│ ├── flashcards_admin.html
│ ├── generador_ejercicios.html
│ └── usuarios_admin.html
└── models/
└── database.py # Modelos de base de datos

text

## 🛠️ Instalación

### Requisitos previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Pasos de instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/tu-usuario/presente-historico.git
cd presente-historico
Crear y activar entorno virtual

bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
Instalar dependencias

bash
pip install -r requirements.txt
Ejecutar la aplicación

bash
python app.py
Abrir en el navegador

text
http://localhost:5001
🔐 Credenciales de Acceso
Administrador
Usuario: admin

Contraseña: admin123

URL: http://localhost:5001/admin/login

Estudiante (registrarse)
Crear cuenta gratuita desde la página de registro

📊 Funcionalidades Principales
1. Clasificador de Textos
Analiza automáticamente cualquier texto y clasifica las oraciones según el tipo de presente verbal utilizado.

2. Reescribidor de Tiempos
Convierte oraciones entre:

Pasado simple → Presente histórico

Futuro → Presente histórico

3. Banco de Ejercicios
100 ejercicios organizados en 9 categorías

Tipos: conversión, completar, identificar, traducción

Seguimiento de progreso guardado en el navegador

4. Flashcards Interactivas
50 tarjetas con conceptos clave

Filtros por categoría y dificultad

Marcado de tarjetas dominadas/difíciles

Atajos de teclado para navegación rápida

5. Dashboard de Estudiante
Estadísticas de progreso

Gráficos por categoría

Rachas de estudio

Logros desbloqueables

Metas personalizables

6. Panel de Administración
CRUD completo de ejercicios

Generador automático de ejercicios

Estadísticas de uso

Gestión de usuarios

🎓 Contenido Educativo
Categorías de Ejercicios
Presente Histórico (20 ejercicios)

Presente por Futuro (10 ejercicios)

Presente Habitual (10 ejercicios)

Presente Actual (10 ejercicios)

Identificación de Categorías (15 ejercicios)

Conversión Avanzada (10 ejercicios)

Narrativa Personal (10 ejercicios)

Ejercicios Mixtos (10 ejercicios)

Traducción Contextual (5 ejercicios)

Flashcards por Categoría
Presente Histórico (4 tarjetas)

Presente por Futuro (3 tarjetas)

Presente Habitual (3 tarjetas)

Presente Actual (3 tarjetas)

Presente Noómico (3 tarjetas)

Y más categorías...

🏆 Sistema de Logros
Logro	Requisito
🌟 Principiante	10 flashcards vistas
🗺️ Explorador	25 flashcards vistas
🏆 Maestro Explorador	50 flashcards vistas
📚 Estudiante Dedicado	10 flashcards dominadas
🎓 Experto en Presente	25 flashcards dominadas
👑 Maestro del Presente	40+ flashcards dominadas
✍️ Practicante	20 ejercicios completados
🏅 Experto en Ejercicios	50 ejercicios completados
🥇 Campeón	80+ ejercicios completados
🤝 Contribuciones
Las contribuciones son bienvenidas. Por favor:

Fork el proyecto

Crea tu rama de características (git checkout -b feature/AmazingFeature)

Commit tus cambios (git commit -m 'Add some AmazingFeature')

Push a la rama (git push origin feature/AmazingFeature)

Abre un Pull Request


🙏 Agradecimientos
Basado en los trabajos de Beatriz Escalante "Redacción para Escritores y Periodistas"

Bootstrap por el framework CSS

Flask por el framework web

⭐ ¡No olvides darle una estrella al repositorio si te fue útil!
https://github.com/Hernank10/presente_historico-.git

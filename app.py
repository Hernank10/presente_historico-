from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import re
import json
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta_aqui'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///frases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
import json
import os

# ... (código existente)

# Cargar ejercicios desde JSON
def cargar_ejercicios():
    ruta_json = os.path.join(os.path.dirname(__file__), 'data', 'ejercicios.json')
    try:
        with open(ruta_json, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        return None

# Nueva ruta para la página de ejercicios
@app.route('/ejercicios')
def ejercicios():
    """Página de ejercicios"""
    return render_template('ejercicios.html')

# API para obtener ejercicios
@app.route('/api/ejercicios', methods=['GET'])
def api_ejercicios():
    """Endpoint para obtener todos los ejercicios"""
    ejercicios = cargar_ejercicios()
    if ejercicios:
        return jsonify(ejercicios)
    return jsonify({'error': 'No se pudieron cargar los ejercicios'}), 500

# API para verificar respuesta de ejercicio
@app.route('/api/ejercicios/verificar', methods=['POST'])
def api_verificar_ejercicio():
    """Endpoint para verificar una respuesta"""
    data = request.get_json()
    ejercicio_id = data.get('ejercicio_id')
    respuesta = data.get('respuesta', '').strip()
    
    ejercicios = cargar_ejercicios()
    if not ejercicios:
        return jsonify({'error': 'No se pudieron cargar los ejercicios'}), 500
    
    # Buscar el ejercicio
    ejercicio_encontrado = None
    for categoria in ejercicios['categorias']:
        for ejercicio in categoria['ejercicios']:
            if ejercicio['id'] == ejercicio_id:
                ejercicio_encontrado = ejercicio
                break
        if ejercicio_encontrado:
            break
    
    if not ejercicio_encontrado:
        return jsonify({'error': 'Ejercicio no encontrado'}), 404
    
    # Normalizar respuestas para comparación
    def normalizar(texto):
        return texto.lower().strip().replace('¿', '').replace('?', '').replace('¡', '').replace('!', '')
    
    es_correcta = normalizar(respuesta) == normalizar(ejercicio_encontrado['respuesta_correcta'])
    
    return jsonify({
        'correcta': es_correcta,
        'respuesta_correcta': ejercicio_encontrado['respuesta_correcta']
    })


# Modelo de datos para frases guardadas
class Frase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500), nullable=False)
    categoria = db.Column(db.String(50))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    user_session = db.Column(db.String(100))
    
    def to_dict(self):
        return {
            'id': self.id,
            'texto': self.texto,
            'categoria': self.categoria,
            'fecha': self.fecha.strftime('%Y-%m-%d %H:%M')
        }

# Funciones de procesamiento lingüístico
def detectar_categoria(oracion):
    """Detecta la categoría del tiempo verbal"""
    oracion_lower = oracion.lower()
    
    # Patrones para presente histórico (fechas pasadas con verbos en presente)
    patron_historico = r'\b\d{3,4}\b'
    if re.search(patron_historico, oracion) and tiene_verbo_presente(oracion):
        return "Presente Histórico"
    
    # Presente por futuro
    palabras_futuro = ['mañana', 'próximo', 'semana que viene', 'el año próximo', 'esta noche']
    if any(palabra in oracion_lower for palabra in palabras_futuro) and tiene_verbo_presente(oracion):
        return "Presente por Futuro"
    
    # Presente habitual
    palabras_habitual = ['siempre', 'nunca', 'todos los', 'cada', 'regularmente']
    if any(palabra in oracion_lower for palabra in palabras_habitual):
        return "Presente Habitual"
    
    # Presente actual
    if 'ahora' in oracion_lower or 'en este momento' in oracion_lower:
        return "Presente Actual"
    
    # Verbos en presente con fechas pasadas
    if tiene_verbo_presente(oracion) and re.search(r'\b\d{3,4}\b', oracion):
        return "Posible Presente Histórico"
    
    return "No identificado"

def tiene_verbo_presente(oracion):
    """Detecta si hay verbos conjugados en presente"""
    terminaciones_presente = ['o', 'as', 'a', 'amos', 'áis', 'an', 'es', 'e', 'imos', 'ís', 'en']
    palabras = re.findall(r'\b[a-zA-Záéíóúñü]+\b', oracion.lower())
    
    for palabra in palabras:
        if any(palabra.endswith(terminacion) for terminacion in terminaciones_presente):
            return True
    return False

def convertir_pasado_a_historico(texto):
    """Convierte texto en pasado a presente histórico"""
    patrones = [
        (r'\b([a-zA-Záéíóúñü]*)ó\b', r'\1a'),  # cantó -> canta
        (r'\b([a-zA-Záéíóúñü]*)aron\b', r'\1an'),  # cantaron -> cantan
        (r'\b([a-zA-Záéíóúñü]*)ieron\b', r'\1en'),  # comieron -> comen
        (r'\b([a-zA-Záéíóúñü]*)í\b', r'\1o'),  # comí -> como
        (r'\b([a-zA-Záéíóúñü]*)aste\b', r'\1as'),  # cantaste -> cantas
        (r'\b([a-zA-Záéíóúñü]*)iste\b', r'\1es'),  # comiste -> comes
        (r'\b([a-zA-Záéíóúñü]*)imos\b', r'\1imos'),  # comimos -> comimos
    ]
    
    texto_transformado = texto
    for patron, reemplazo in patrones:
        texto_transformado = re.sub(patron, reemplazo, texto_transformado, flags=re.IGNORECASE)
    
    return texto_transformado

def convertir_futuro_a_historico(texto):
    """Convierte texto en futuro a presente histórico"""
    patrones = [
        (r'\b([a-zA-Záéíóúñü]*)é\b', r'\1o'),  # cantaré -> canto
        (r'\b([a-zA-Záéíóúñü]*)ás\b', r'\1as'),  # cantarás -> cantas
        (r'\b([a-zA-Záéíóúñü]*)á\b', r'\1a'),  # cantará -> canta
        (r'\b([a-zA-Záéíóúñü]*)emos\b', r'\1emos'),  # cantaremos -> cantamos
        (r'\b([a-zA-Záéíóúñü]*)án\b', r'\1an'),  # cantarán -> cantan
    ]
    
    texto_transformado = texto
    for patron, reemplazo in patrones:
        texto_transformado = re.sub(patron, reemplazo, texto_transformado, flags=re.IGNORECASE)
    
    return texto_transformado

def obtener_color_categoria(categoria):
    """Retorna el color Bootstrap según la categoría"""
    colores = {
        'Presente Histórico': 'primary',
        'Presente por Futuro': 'success',
        'Presente Habitual': 'warning',
        'Presente Actual': 'info',
        'Posible Presente Histórico': 'secondary'
    }
    return colores.get(categoria, 'secondary')

# Rutas de la aplicación
@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/teoria')
def teoria():
    """Página de teoría"""
    return render_template('teoria.html')

@app.route('/clasificador')
def clasificador():
    """Página del clasificador"""
    return render_template('clasificador.html')

@app.route('/reescritor')
def reescritor():
    """Página del reescritor"""
    return render_template('reescritor.html')

@app.route('/practica')
def practica():
    """Página de práctica"""
    return render_template('practica.html')

# API Endpoints
@app.route('/api/clasificar', methods=['POST'])
def api_clasificar():
    """Endpoint para clasificar texto"""
    data = request.get_json()
    texto = data.get('texto', '')
    
    if not texto:
        return jsonify({'error': 'No se proporcionó texto'}), 400
    
    # Dividir en oraciones
    oraciones = re.split(r'[.!?]+', texto)
    oraciones = [o.strip() for o in oraciones if o.strip()]
    
    resultados = []
    for i, oracion in enumerate(oraciones, 1):
        categoria = detectar_categoria(oracion)
        color = obtener_color_categoria(categoria)
        resultados.append({
            'numero': i,
            'texto': oracion,
            'categoria': categoria,
            'color': color
        })
    
    return jsonify({'resultados': resultados})

@app.route('/api/reescribir', methods=['POST'])
def api_reescribir():
    """Endpoint para reescribir texto"""
    data = request.get_json()
    texto = data.get('texto', '')
    modo = data.get('modo', 'pasado')  # 'pasado' o 'futuro'
    
    if not texto:
        return jsonify({'error': 'No se proporcionó texto'}), 400
    
    if modo == 'pasado':
        texto_transformado = convertir_pasado_a_historico(texto)
    else:
        texto_transformado = convertir_futuro_a_historico(texto)
    
    return jsonify({
        'original': texto,
        'transformado': texto_transformado,
        'modo': modo
    })

@app.route('/api/frases', methods=['GET', 'POST'])
def api_frases():
    """Endpoint para gestionar frases"""
    # Obtener o crear ID de sesión
    if 'user_id' not in session:
        session['user_id'] = os.urandom(16).hex()
    
    user_session = session['user_id']
    
    if request.method == 'POST':
        data = request.get_json()
        texto = data.get('texto', '')
        
        if not texto:
            return jsonify({'error': 'No se proporcionó texto'}), 400
        
        if len(texto) > 500:
            return jsonify({'error': 'El texto no puede exceder 500 caracteres'}), 400
        
        # Verificar límite de 100 frases por usuario
        count = Frase.query.filter_by(user_session=user_session).count()
        if count >= 100:
            return jsonify({'error': 'Has alcanzado el límite de 100 frases'}), 400
        
        categoria = detectar_categoria(texto)
        nueva_frase = Frase(
            texto=texto,
            categoria=categoria,
            user_session=user_session
        )
        db.session.add(nueva_frase)
        db.session.commit()
        
        return jsonify({
            'id': nueva_frase.id,
            'texto': nueva_frase.texto,
            'categoria': nueva_frase.categoria,
            'fecha': nueva_frase.fecha.strftime('%Y-%m-%d %H:%M')
        })
    
    else:  # GET
        frases = Frase.query.filter_by(user_session=user_session).order_by(Frase.fecha.desc()).all()
        return jsonify({
            'frases': [f.to_dict() for f in frases],
            'total': len(frases)
        })

@app.route('/api/frases/<int:id>', methods=['DELETE'])
def api_eliminar_frase(id):
    """Endpoint para eliminar una frase"""
    if 'user_id' not in session:
        return jsonify({'error': 'No autorizado'}), 401
    
    frase = Frase.query.get_or_404(id)
    
    if frase.user_session != session['user_id']:
        return jsonify({'error': 'No autorizado'}), 401
    
    db.session.delete(frase)
    db.session.commit()
    
    return jsonify({'success': True})

@app.route('/api/frases/limpiar', methods=['DELETE'])
def api_limpiar_frases():
    """Endpoint para eliminar todas las frases del usuario"""
    if 'user_id' not in session:
        return jsonify({'error': 'No autorizado'}), 401
    
    Frase.query.filter_by(user_session=session['user_id']).delete()
    db.session.commit()
    
    return jsonify({'success': True})

# Crear tablas de la base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

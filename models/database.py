from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Frase(db.Model):
    __tablename__ = 'frases'
    
    id = db.Column(db.Integer, primary_key=True)
    texto = db.Column(db.String(500), nullable=False)
    categoria = db.Column(db.String(50))
    fecha = db.Column(db.DateTime, default=datetime.utcnow)
    user_session = db.Column(db.String(100), index=True)
    
    def to_dict(self):
        return {
            'id': self.id,
            'texto': self.texto,
            'categoria': self.categoria,
            'fecha': self.fecha.strftime('%Y-%m-%d %H:%M')
        }
    
    def __repr__(self):
        return f'<Frase {self.id}: {self.texto[:50]}>'

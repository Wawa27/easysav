from easysav import db
from sqlalchemy_serializer import SerializerMixin


class Intervention(db.Model, SerializerMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_id = db.Column(db.Integer)
    piece = db.Column(db.String(32))
    problem = db.Column(db.String(64))

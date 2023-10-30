from src import db, app
from flask_migrate import Migrate

class Vyras(db.Model):
    __tablename__ = 'vyrai'
    id = db.Column(db.Integer, primary_key=True)
    vardas = db.Column(db.String(80), nullable=False)
    team = db.Column(db.String(80), nullable=False)
    amzius = db.Column(db.String(120), unique=True, nullable=False)
    ugis = db.Column(db.Text, nullable=False)
    svoris = db.Column(db.Text, nullable=False)

    def __init__(self, vardas, team, amzius, ugis, svoris):
        self.vardas = vardas
        self.team = team
        self.amzius = amzius
        self.ugis = ugis
        self.svoris = svoris

    def __repr__(self):
        return f'{self.vardas} - {self.svoris}'

Migrate(app, db)

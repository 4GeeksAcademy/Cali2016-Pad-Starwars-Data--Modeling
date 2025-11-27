from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    is_active = db.Column(db.Boolean(), nullable=False)

    favorites = db.relationship("Favorite", backref="user", lazy=True)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
        }


class Planet(db.Model):
    __tablename__ = 'planet'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    climate = db.Column(db.String(120))
    population = db.Column(db.Integer)

    favorites = db.relationship("Favorite", backref="planet", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "climate": self.climate,
            "population": self.population
        }


class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    height = db.Column(db.String(20))
    gender = db.Column(db.String(20))

    favorites = db.relationship("Favorite", backref="character", lazy=True)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.height,
            "gender": self.gender
        }


class Favorite(db.Model):
    __tablename__ = 'favorite'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    planet_id = db.Column(db.Integer, db.ForeignKey("planet.id"), nullable=True)
    character_id = db.Column(db.Integer, db.ForeignKey("character.id"), nullable=True)

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "character_id": self.character_id
        }

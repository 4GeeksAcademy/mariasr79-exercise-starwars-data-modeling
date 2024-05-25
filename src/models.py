import os
from pyclbr import Function
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class User(Base):
     __tablename__ = 'user'
     Id = Column(Integer, primary_key = True)
     username = Column(String(20), nullable=False, unique=True)
     Name = Column(String(20), nullable = False, unique = True)
     LastName = Column(String(20), nullable = False, unique = True)
     Email = Column(String(50), nullable = False, unique = True)
     Password =  Column(String(100), nullable=False)
     DateOfSuscription = Column("DateTime", default=func.now())
     favorite_characters = relationship('Character', secondary="favorite_characters")
     favorite_planets = relationship('Planet', secondary="favorite_planets")

class Character(Base):
     __tablename__ = 'character'
     Id = Column(Integer, primary_key = True)
     Name = Column(String(50), nullable = False)
     Description = Column(String(250))

class Favourites(Base):
     __tablename__ = 'favourites'
     Id = Column(Integer, primary_key = True)
     user_id = Column(Integer, ForeignKey('user.id'))
     Character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
     Planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
     User = relationship(User, secundary='User')
     Character = relationship(Character, secundary='Character')
     Planet = relationship("Planet", secundary='Planet')
    
class Planets(Base):
     __tablename__ = 'planets'
     Id = Column(Integer, primary_key = True)
     Name = Column(String(50), nullable = False)
     Climate = Column(String(50))
     Terrain = Column(String(50))
     Favourites = relationship(Favourites, secundary='Favourites')
     Character = relationship(Character, secundary='Character')

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')

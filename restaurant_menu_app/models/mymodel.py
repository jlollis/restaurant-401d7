from sqlalchemy import (
    Boolean,
    Column,
    Float,
    Integer,
    Unicode,
)

from .meta import Base


class Appetizer(Base):
    __tablename__ = 'appetizers'
    id = Column(Integer, primary_key=True)  # int
    name = Column(Unicode)  # str
    cost = Column(Float(precision=2))  # float
    description = Column(Unicode)  # str
    spiciness = Column(Integer)  # int
    special = Column(Boolean, default=False)  # bool

    def __repr__(self):
        return '<Appetizer: {}>'.format(self.name)


class Entree(Base):
    __tablename__ = 'entrees'
    id = Column(Integer, primary_key=True)  # int
    name = Column(Unicode)  # str
    cost = Column(Float(precision=2))  # float
    description = Column(Unicode)  # str
    spiciness = Column(Integer)  # int
    special = Column(Boolean, default=False)  # bool

    def __repr__(self):
        return '<Entree: {}>'.format(self.name)


class Drink(Base):
    __tablename__ = 'drinks'
    id = Column(Integer, primary_key=True)  # int
    name = Column(Unicode)  # str
    cost = Column(Float(precision=2))  # float
    description = Column(Unicode)  # str
    proof = Column(Float)
    special = Column(Boolean, default=False)  # bool

    def __repr__(self):
        return '<Drink: {}>'.format(self.name)

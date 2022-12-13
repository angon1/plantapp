# obiekt dla modelu plant
from sqlalchemy import Column, Integer, String

from . import Base


class Plant(Base):
    __tablename__ = "custom plant"
    id = Column(Integer, primary_key=True)
    name = Column(String)

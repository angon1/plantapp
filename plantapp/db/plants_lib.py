from sqlalchemy import Column, Integer, String

from . import Base


class PlantsLib(Base):
    __tablename__ = "plantsLibrary"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    alternate_name = Column(String)
    sow_instruction = Column(String)
    space_instructions = Column(String)
    harverst_instructions = Column(String)
    compatible_plants = Column(String)
    avoid_instructions = Column(String)
    culinary_hints = Column(String)
    culinary_preservation = Column(String)
    url = Column(String)

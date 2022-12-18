import json

from sqlalchemy import Column, Integer, String

from . import Base


class PlantsLib(Base):
    __tablename__ = "plants library"
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

    def __repr__(self) -> str:
        return json.dumps(dict(self), ensure_ascii=False)

    @classmethod
    def get_by_name(cls, name):
        return cls.query().filter_by(name=name).first()

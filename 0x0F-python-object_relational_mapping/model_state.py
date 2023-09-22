from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
"""model state phase 1"""

Base = declarative_base()


class state(Base):
    """first edition of state model"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

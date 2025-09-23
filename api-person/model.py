from database import Base
from sqlalchemy import Column,Integer,String,Float,Boolean
class Person(Base):
    __tablename__="db_person"
    Id= Column(Integer, primary_key=True, index=True)
    Name = Column(String, index=True,nullable=False)
    EnglishName = Column(String, index=True,nullable=False)
    Email = Column(String, index=True,nullable=False)
    Age = Column(Integer) 
    Address = Column(String,nullable=False)
    Is_Active = Column(Boolean,nullable=False)
    Phone = Column(String, index=True,nullable=False)
    Phone1 = Column(String, index=True)
    
    
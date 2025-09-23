from pydantic import BaseModel
from typing import Optional
class Person:
    Id: int
    Name: str
    EnglishName : Optional[str] 
    Email : Optional[str] = None
    Age : int 
    Address : Optional[str] = None
    Is_Active : bool = True
    Phone : Optional[str] = None
    Phone1 : Optional[str] = None
    
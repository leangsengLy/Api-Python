import dataModel
class PersonDto(dataModel.Person):
    id: int
    class Config:
        orm_mode = True
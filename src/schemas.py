from datetime import date as birth_date

from pydantic import BaseModel, Field, EmailStr


class ContactModel(BaseModel):
    name: str = Field(min_length=2, max_length=15)
    surname: str = Field(min_length=2, max_length=15)
    email: EmailStr
    phone: str = Field(min_length=6, max_length=16)
    birthday: birth_date
    additionally: str = Field(min_length=3, max_length=300)


class ResponseContact(BaseModel):
    id: int = 1
    name: str = "Vitalii"
    surname: str = "Zatoka"
    email: EmailStr = "zatokav@gmail.com"
    phone: str = "+380937896541"
    birthday: birth_date = birth_date(year=1993, month=2, day=11)
    additionally: str = "A very nice contact"

    class Config:
        orm_mode = True

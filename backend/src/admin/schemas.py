from pydantic import BaseModel

class UserOut(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    role: str

    class Config:
        orm_mode = True

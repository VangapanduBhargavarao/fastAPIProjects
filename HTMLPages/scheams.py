from models import Base
from pydantic import BaseModel
from sqlalchemy import Integer,String,Column



class User(Base):
    __tablename__="info"
    fname:int=Column(String(200),nullable=False)
    lname:int=Column(String(200),nullable=False)
    phone_number:str=Column(String(200),nullable=False,primary_key=True,index=True)
    email:str=Column(String(200),nullable=False)
    zipcode:str=Column(String(200),nullable=False)



class RequestData(BaseModel):
    fname:str
    lname:str
    phone_number:str
    email:str
    zipcode:str

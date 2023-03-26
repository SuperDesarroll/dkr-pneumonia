from typing import Optional , List
from pydantic import BaseModel
from models import Post,User
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay

class UserValidate(BaseModel):
    name:str
    email:str
    password:str

class Geo(BaseModel):
    lat:str
    lng:str 

class Address(BaseModel):
    geo:Geo
    city:str
    suite:str
    street:str
    zipcode:str

class Company(BaseModel):
    bs:str
    name:str
    catchPhrase:str

class ShowUser(BaseModel):
    name:str
    username:str
    email:str
    address:Address
    phone:str
    website:str
    company:Company
    class Config():
        orm_mode = True

class ShowAlbum(BaseModel):
    userId:int
    id:int 
    title:str 
    class Config():
        orm_mode = True

class AlbumValidate(BaseModel):
    title:str
    userId:int

class ShowPost(BaseModel):
    userId:int
    id:int 
    title:str
    body:str 
    class Config():
        orm_mode = True

class PostValidate(BaseModel):
    userId:int
    title:str
    body:str 

class PostValidatePatch(BaseModel):
    userId:Optional[int] 
    title:Optional[str] 
    body:Optional[str]
 
class ShowCommentByPost(BaseModel):
    postId:int
    id:int
    name:str
    email:str
    body:str
    class Config():
        orm_mode = True


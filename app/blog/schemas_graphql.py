import graphene
from graphene import String,Int
from models import Post,User,Album
from graphene_sqlalchemy import SQLAlchemyObjectType
from graphene import relay

class PostModel(SQLAlchemyObjectType):
    id = Int()
    class Meta:
        model = Post

class AlbumModel(SQLAlchemyObjectType):
    id = Int()
    class Meta:
        model = Album
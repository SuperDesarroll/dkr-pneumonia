from starlette.graphql import GraphQLApp
from blog.schemas import *
from blog.schemas_graphql import *
import graphene
from blog.database import get_db, SessionLocal
from sqlalchemy.orm import Session
from blog.repository import post, album
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField


class Query(graphene.ObjectType):
    all_posts = graphene.List(PostModel)

    post_by_id = graphene.Field(PostModel, post_id=graphene.Int(required=True))

    all_albums = graphene.List(AlbumModel)

    def resolve_all_posts(self, info):
        query = PostModel.get_query(info)
        return query.all()

    def resolve_all_albums(self, info):
        query = AlbumModel.get_query(info)
        return query.all()

    def resolve_post_by_id(self, info, post_id):
        db = SessionLocal()
        return db.query(Post).filter(Post.id == post_id).first()


class CreateNewPost(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        body = graphene.String(required=True)
        userId = graphene.Int(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, title, body, userId):
        new_post = PostValidate(title=title, body=body, userId=userId)
        post.create_post(new_post, SessionLocal())
        ok = True
        return CreateNewPost(ok=ok)


class CreateNewAlbum(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        userId = graphene.Int(required=True)
    ok = graphene.Boolean()

    @staticmethod
    def mutate(root, info, title, userId):
        new_album = AlbumValidate(title=title, userId=userId)
        album.create_album(new_album, SessionLocal())
        ok = True
        return CreateNewAlbum(ok=ok)


class PostMutations(graphene.ObjectType):
    create_new_post = CreateNewPost.Field()
    create_new_album = CreateNewAlbum.Field()

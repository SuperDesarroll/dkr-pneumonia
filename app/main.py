from fastapi import FastAPI
from blog.routers import jsonPlaceHolder, user, album, post, comments
from blog.repository import graphql
import graphene
from starlette.graphql import GraphQLApp

app = FastAPI()
app.include_router(jsonPlaceHolder.router)
app.include_router(user.router)
app.include_router(album.router)
app.include_router(post.router)
app.include_router(comments.router)
app.add_route(
    "/graphql",
    GraphQLApp(
        schema=graphene.Schema(
            query=graphql.Query,
            mutation=graphql.PostMutations),
        graphiql=True))
# app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=graphql.Query, mutation=graphql.PostMutations)))

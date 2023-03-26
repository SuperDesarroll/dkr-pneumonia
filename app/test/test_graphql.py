from graphene.test import Client
import pytest
from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK
import sys
import os 
import graphene
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from main import app
from blog.repository import graphql
# from models import Post,User 
from orator import DatabaseManager, Model, Schema
from orator.migrations import DatabaseMigrationRepository, Migrator
# @pytest.fixture(autouse=True)
# def client() -> Client:
#     "start the client"
#     return Client(app)

@pytest.fixture(autouse=True)
def setup_database():
    DATABASES = {
        "sqlite": {
            "driver": "sqlite",
            "database": "test.db"
        }
    }

    db = DatabaseManager(DATABASES)
    Schema(db)

    Model.set_connection_resolver(db)

    repository = DatabaseMigrationRepository(db, "migrations")
    migrator = Migrator(repository, db)

    if not repository.repository_exists():
        repository.create_repository()

    migrator.reset("migrations")
    migrator.run("migrations")

@pytest.fixture(scope="module")
def client():
    client = Client(schema=graphene.Schema(query=graphql.Query, mutation=graphql.PostMutations))
    return client

def test_mutation_post(client:TestClient):
    query = """
        mutation {
            createNewAlbum(title:"Este es un nuevo postssssssssssssssssssssssssssssssss",userId:1) {
                ok
            }
        }
    """
    result = client.execute(query)
    assert result["data"]["createNewAlbum"]["ok"] == True

def test_query_post(client:TestClient):
    query = """
        query{
            allAlbums{
                title
            }
        }
    """
    result = client.execute(query)
    assert len(result["data"]["allAlbums"]) > 0 
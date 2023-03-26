import pytest
from starlette.testclient import TestClient
from starlette.status import HTTP_200_OK
import sys
import os 

sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from main import app
# from models import Post,User 

@pytest.fixture(scope="function")
def client() -> TestClient:
    "start the client"
    return TestClient(app)

# @pytest.fixture()
# def setUp(client:TestClient):

#     response_user = client.post('/jsonPlaceHolder/crea_users')
#     print(response_user)
def test_user(client:TestClient):
    response_user = client.post('/jsonPlaceHolder/crea_users')
    assert response_user.json()["respuesta"]=='Usuarios creados satisfactoriamente!'

def test_todos(client:TestClient):
    response = client.post('/jsonPlaceHolder/crea_todos')
    assert response.json()["respuesta"]=='Todos creados satisfactoriamente!'

def test_album(client:TestClient):
    response =  client.post('/jsonPlaceHolder/crea_albums')
    assert response.json()["respuesta"]=='Albumns creados satisfactoriamente!'

def test_fotos(client:TestClient):
    response = client.post('/jsonPlaceHolder/crea_fotos')
    assert response.json()["respuesta"]=='Photos creados satisfactoriamente!'

def test_post(client:TestClient):
    response = client.post('/jsonPlaceHolder/crea_post')
    assert response.json()["respuesta"]=='Post creados satisfactoriamente!'

def test_comentarios(client:TestClient):
    response = client.post('/jsonPlaceHolder/crea_comentarios')
    assert response.json()["respuesta"]=='Comments creados satisfactoriamente!'

def test_elimina_todo(client:TestClient):
    response =  client.delete('/jsonPlaceHolder/elimina_todo')
    assert response.json()["respuesta"] == 'Todo eliminado con exito!'

def test_crea_todo(client:TestClient):
    response =  client.post('/jsonPlaceHolder/crear_todo')
    assert response.json()["respuesta"] =='Todo creado con exito!'

def test_user_id(client:TestClient):
    response = client.get('/user/1')
    assert "name" in response.json()
    assert response.json()["email"] == 'Sincere@april.biz'

def test_album_id(client:TestClient):
    response = client.get('/album/1')
    assert "title" in response.json()
    assert response.json()["title"] == 'quidem molestiae enim'
    assert response.json()["userId"] == 1

def test_post_id(client:TestClient):
    response = client.get('/posts/1')
    assert "title" in response.json()
    assert response.json()["id"] == 1

def test_post_update(client:TestClient):
    data = {
        "userId": 6,
        "title": "Este es el nuevo title",
        "body": "Este es el nuevo body"
    }
    response = client.put('/posts/1',json=data)
    assert response.json()["respuesta"] == 'Actualizado'
    response = client.get('/posts/1')
    assert response.json()["userId"] == 6
    assert response.json()["title"] == 'Este es el nuevo title'
    assert response.json()["body"] == 'Este es el nuevo body'

def test_post_delete(client:TestClient):
    response = client.delete('/posts/100')
    assert response.json()["Respuesta"] == '100 eliminado con exito!'
    response = client.get('/posts/100')
    assert response.json()["detail"] == 'No existe el post con el id 100 por favor vuelva a crear los post'

def test_post_patch(client:TestClient):
    data = {
        "body": "Este es el nuevo body del id 2"
    }
    response = client.patch('/posts/2',json=data)
    assert response.json()["respuesta"] == "Actualizado"
    response = client.get('/posts/2')
    assert response.json()["userId"] == 1
    assert response.json()["title"] == 'qui est esse'
    assert response.json()["body"] == 'Este es el nuevo body del id 2'

def test_post_comments(client:TestClient):
    response = client.get('/posts/1/comments')
    assert len(response.json()) == 5

def test_create_post(client:TestClient):
    data = {
        "userId": 2,
        "title": "hola desde el title",
        "body": "hola desde el body"
    }
    response = client.post('/posts/',json=data)
    assert response.json()["id"] == 101

def test_comments_post(client:TestClient):
    response = client.get('/comments/?postId=3')
    assert len(response.json())==5

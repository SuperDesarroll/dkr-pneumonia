from fastapi import APIRouter, Depends, Response, HTTPException, status
from blog.schemas import *
from models import *
from blog.database import get_db, SessionLocal
from sqlalchemy.orm import Session
import requests
from blog.repository.jsonPlaceHolder import *

router = APIRouter(
    prefix='/jsonPlaceHolder',
    tags=['PlaceHolder Api']
)


@router.post('/crear_todo')
def create_all():
    '''
        Esta funcion crea todo
    '''
    # url = "http://localhost:8000"
    # # url_ =f'{url}/jsonPlaceHolder/crea_users'
    # requests.post(f'{url}/jsonPlaceHolder/crea_users')
    # requests.post(f'{url}/jsonPlaceHolder/crea_todos')
    # requests.post(f'{url}/jsonPlaceHolder/crea_albums')
    # requests.post(f'{url}/jsonPlaceHolder/crea_fotos')
    # requests.post(f'{url}/jsonPlaceHolder/crea_post')
    # requests.post(f'{url}/jsonPlaceHolder/crea_comentarios')
    create_users(SessionLocal())
    create_todos(SessionLocal())
    create_albums(SessionLocal())
    create_fotos(SessionLocal())
    create_posts(SessionLocal())
    create_comments(SessionLocal())
    return {"respuesta": "Todo creado con exito!"}


@router.post('/crea_users')
def create_users(db: Session = Depends(get_db)):
    '''
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/users
        y llenar la tabla de postgres users
    '''
    r = requests.get('https://jsonplaceholder.typicode.com/users')
    delete_all_users(db)
    for user in r.json():
        create_user(user, db)
    db.execute(
        """ SELECT SETVAL('public."users_id_seq"', COALESCE(MAX(id), 1)) FROM users""")
    return {"respuesta": "Usuarios creados satisfactoriamente!"}


@router.post('/crea_todos')
def create_todos(db: Session = Depends(get_db)):
    '''
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/todos
        y llenar la tabla de postgres todos
    '''
    r = requests.get('https://jsonplaceholder.typicode.com/todos')
    delete_all_todos(db)
    for todo in r.json():
        create_todo(todo, db)
    db.execute(
        """ SELECT SETVAL('public."todos_id_seq"', COALESCE(MAX(id), 1)) FROM todos""")
    return {"respuesta": "Todos creados satisfactoriamente!"}


@router.post('/crea_albums')
def create_albums(db: Session = Depends(get_db)):
    '''
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/albums
        y llenar la tabla de postgres albums
    '''
    r = requests.get('https://jsonplaceholder.typicode.com/albums')
    delete_all_albums(db)
    for album in r.json():
        create_album(album, db)
    db.execute(
        """ SELECT SETVAL('public."album_id_seq"', COALESCE(MAX(id), 1)) FROM album""")
    return {"respuesta": "Albumns creados satisfactoriamente!"}


@router.post('/crea_fotos')
def create_fotos(db: Session = Depends(get_db)):
    '''
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/photos
        y llenar la tabla de postgres photos
    '''
    r = requests.get('https://jsonplaceholder.typicode.com/photos')
    delete_all_photos(db)
    for photo in r.json():
        create_photos(photo, db)
    db.execute(
        """ SELECT SETVAL('public."photo_id_seq"', COALESCE(MAX(id), 1)) FROM photo""")
    return {"respuesta": "Photos creados satisfactoriamente!"}


@router.post('/crea_post')
def create_posts(db: Session = Depends(get_db)):
    '''
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/posts
        y llenar la tabla de postgres post
    '''
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    delete_all_post(db)
    for post in r.json():
        create_post(post, db)
    db.execute(""" SELECT SETVAL('public."post_id_seq"', COALESCE(MAX(id), 1)) FROM post""")  # Actualiza la secuencia autoincrementable
    return {"respuesta": "Post creados satisfactoriamente!"}


@router.post('/crea_comentarios')
def create_comments(db: Session = Depends(get_db)):
    '''
        Esta funcion se encarga de realizar la peticion a la api https://jsonplaceholder.typicode.com/comments
        y llenar la tabla de postgres comments
    '''
    r = requests.get('https://jsonplaceholder.typicode.com/comments')
    delete_all_comments(db)
    for comment in r.json():
        create_comment(comment, db)
    # SELECT SETVAL('public."post_id_seq"', COALESCE(MAX(id), 1)) FROM
    # public.post;
    db.execute(
        """ SELECT SETVAL('public."comment_id_seq"', COALESCE(MAX(id), 1)) FROM comment""")
    return {"respuesta": "Comments creados satisfactoriamente!"}


@router.delete('/elimina_todo')
def delete_all(db: Session = Depends(get_db)):
    '''
        Elimina todo lo que hay en las tablas solo elimina en usuarios pero como esta en cascade elimina todo lo demas
    '''
    delete_all_users(db)
    return {"respuesta": "Todo eliminado con exito!"}

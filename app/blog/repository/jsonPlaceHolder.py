from sqlalchemy.orm import Session 
from models import *
from fastapi import HTTPException,status
from blog.repository.user import show_user
from blog.repository.album import show_album
from blog.repository.post import show_post
import requests

url_request = 'http://localhost:8000/'

def create_user(user,db:Session):
    ''' 
        Esta funcion primero crea los usuarios
    '''
    new_user = User(id = user["id"],name=user["name"],username=user["username"],email=user["email"],address=user["address"],phone=user["phone"],website=user["website"],company=user["company"])
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

def delete_all_users(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla users
    '''
    db.query(User).delete()
    db.commit()

def create_todo(todo,db:Session):
    ''' 
        Esta funcion crea el registro en la tabla todo
    ''' 
    show_user(todo["userId"],db)
    new_todo = Todo(id = todo["id"],title=todo["title"],completed=todo["completed"],userId=todo["userId"])
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    
def delete_all_todos(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla todos
    '''
    db.query(Todo).delete()
    db.commit()

def create_album(album,db:Session):
    ''' 
        Esta funcion crea todos los albums
    '''
    show_user(album["userId"],db)
    new_album = Album(id = album["id"],title=album["title"],userId=album["userId"])
    db.add(new_album)
    db.commit()
    db.refresh(new_album)

def delete_all_albums(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla albums
    '''
    db.query(Album).delete()
    db.commit()

def create_photos(photo,db:Session):
    ''' 
        Esta funcion crea el registro en la tabla photo
    '''
    show_album(photo["albumId"],db)
    new_photo = Photo(id = photo["id"],title=photo["title"],url=photo["url"],albumId=photo["albumId"],thumbnailUrl=photo["thumbnailUrl"])
    db.add(new_photo)
    db.commit()
    db.refresh(new_photo)

def delete_all_photos(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla photos
    ''' 
    db.query(Photo).delete()
    db.commit()

def create_post(post,db:Session):
    ''' 
        Esta funcion crea el registro en la tabla post
    '''

    show_user(post["userId"],db)
    new_post = Post(id = post["id"],title=post["title"],body=post["body"],userId=post["userId"])
    db.add(new_post)
    db.commit()
    db.refresh(new_post)

def delete_all_post(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla post
    ''' 
    db.query(Post).delete()
    db.commit()

def create_comment(comment,db:Session):
    ''' 
        Esta funcion crea el registro en la tabla post
    '''
    show_post(comment["postId"],db)
    new_comment = Comment(id=comment["id"],name=comment["name"],email=comment["email"],postId=comment["postId"],body=comment["body"])
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

def delete_all_comments(db:Session):
    ''' 
        Esta funcion elimina todos los registros de la tabla comment
    ''' 
    db.query(Comment).delete()
    db.commit()
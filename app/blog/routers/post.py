from fastapi import APIRouter, Depends, Response, HTTPException, status
from blog.schemas import *
from models import *
from blog.database import get_db
from sqlalchemy.orm import Session
import requests
from blog.repository import post
from blog.schemas import *
from typing import List

router = APIRouter(
    prefix='/posts',
    tags=['Posts']
)


@router.get('/{id}', response_model=ShowPost)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    '''
        Esta funcion devuelve un post mediante al id
    '''
    return post.show_post(id, db)


@router.get('/{id}/comments', response_model=List[ShowCommentByPost])
def show_comment_by_post(
        id: int,
        response: Response,
        db: Session = Depends(get_db)):
    '''
        Esta funcion devuelve los comentarios de un post
    '''
    return post.show_comment_by_post(id, db)


@router.post('/', response_model=ShowPost)
def create_post(request: PostValidate, db: Session = Depends(get_db)):
    '''
        Esta funcion crea un post
    '''
    return post.create_post(request, db)


@router.delete('/{id}')
def destroy(id, db: Session = Depends(get_db)):
    '''
        Esta funcion elimina un post
    '''
    return post.delete_post(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: PostValidate, db: Session = Depends(get_db)):
    '''
        Esta funcion actualiza un post
    '''
    return post.update_post(id, request, db)


@router.patch('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_patch(id, request: PostValidatePatch,
                 db: Session = Depends(get_db)):
    '''
        Esta funcion actualiza una actualizacion a un post
    '''
    return post.update_post_patch(id, request, db)

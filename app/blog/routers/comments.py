from fastapi import APIRouter, Depends, Response, HTTPException, status
from blog.schemas import *
from models import *
from blog.database import get_db
from sqlalchemy.orm import Session
import requests
from blog.repository import comments
from blog.schemas import *

router = APIRouter(
    prefix='/comments',
    tags=['Comments']
)


@router.get('/', response_model=List[ShowCommentByPost])
def show_comment_by_post(
        postId: int,
        response: Response,
        db: Session = Depends(get_db)):
    '''
        Esta funcion devuelve todos los comentarios de un post
    '''
    return comments.show_comment_by_post(postId, db)

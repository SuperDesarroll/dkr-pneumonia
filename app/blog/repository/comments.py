from sqlalchemy.orm import Session
from models import *
from fastapi import HTTPException, status
from blog.repository import post


def show_comment_by_post(id: int, db: Session):
    '''
        Esta funcion devuelve todos los comentarios de un post
    '''
    post.show_post(id, db)
    comments_by_post = db.query(Comment).filter(Comment.postId == id).all()
    if len(comments_by_post) == 0:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'El post {id} aun no tiene comentarios')
    return comments_by_post

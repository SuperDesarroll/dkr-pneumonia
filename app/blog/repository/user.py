from sqlalchemy.orm import Session
from models import *
from fastapi import HTTPException, status


def show_user(id, db: Session):
    '''
        Esta funcion devuelve un usuario por el id
    '''
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'No existe el usuario con el id {id}')
    return user

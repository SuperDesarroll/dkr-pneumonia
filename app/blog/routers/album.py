from fastapi import APIRouter, Depends, Response, HTTPException, status
from blog.schemas import *
from models import *
from blog.database import get_db
from sqlalchemy.orm import Session
import requests
from blog.repository.album import *
from blog.schemas import *

router = APIRouter(
    prefix='/album',
    tags=['Albums']
)


@router.get('/{id}', response_model=ShowAlbum)
def show(id: int, response: Response, db: Session = Depends(get_db)):
    '''
        Devuelve un album por el id
    '''
    return show_album(id, db)

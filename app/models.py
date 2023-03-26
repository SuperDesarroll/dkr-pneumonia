from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, String, create_engine
import sys
import os
# sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
# YO ESTOY AFUERA DE APP estoy en la raiz ... debo de ingresar a app para
# coger el blog
from blog.database import Base
# Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    username = Column(String)
    email = Column(String)
    address = Column(JSONB)
    phone = Column(String)
    website = Column(String)
    company = Column(JSONB)
    todos = relationship('Todo', back_populates='creator')
    album = relationship('Album', back_populates='creator_album')
    post = relationship('Post', back_populates='creator_post')


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    completed = Column(Boolean)
    userId = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    creator = relationship('User', back_populates='todos')


class Album(Base):
    __tablename__ = 'album'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    userId = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    creator_album = relationship('User', back_populates='album')
    photo = relationship('Photo', back_populates='creator_photo')


class Photo(Base):
    __tablename__ = 'photo'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    url = Column(String)
    thumbnailUrl = Column(String)
    albumId = Column(Integer, ForeignKey('album.id', ondelete="CASCADE"))
    creator_photo = relationship('Album', back_populates='photo')


class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    body = Column(String)
    userId = Column(Integer, ForeignKey('users.id', ondelete="CASCADE"))
    creator_post = relationship('User', back_populates='post')
    comment = relationship('Comment', back_populates='creator_comment')


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    email = Column(String)
    body = Column(String)
    postId = Column(Integer, ForeignKey('post.id', ondelete="CASCADE"))
    creator_comment = relationship('Post', back_populates='comment')

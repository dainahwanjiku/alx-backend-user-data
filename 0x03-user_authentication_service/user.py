#!/usr/bin/env python3
"""
create a SQLAlchemy model named User for a database table named users
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    
    """this is what is contained in the user class.
    """
    id = Base.Column(Integer, primary_key=True)
    email = Base.Column(String(250), nullable=False)
    hashed_password = Base.Column(String(250), nullable=False)
    session_id = Base.Column(String(250), nullable=True)
    reset_token = Base.Column(String(250), nullable=True)

#!/usr/bin/env python3
"""
create a SQLAlchemy model named User for a database table named users
"""

from sqlalchemy import Column, Integer, String


class User(Base):
    __tablename__ = 'users'
    
    """this is what is contained in the user class.
    """
    id = Column(Integer, primary_key=True)
    email = Column(String, nulliable=False)
    hashed_password = Column(String, nulliable=False)
    session_id = Column(String, nulliable=True)
    reset_token = Column(String, nulliable=True)

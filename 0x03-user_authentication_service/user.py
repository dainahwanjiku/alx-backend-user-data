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
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)

    def __repr__(self):
        return "<User(email='%s', hashed_password='%s', session_id='%s', reset_token='%s')>" % (
                self.email, self.hashed_password, self.session_id, self.reset_token)

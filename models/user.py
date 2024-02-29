#!/usr/bin/python3
""" User class"""

from base_model import BaseModel
class User(BaseModel):
    """Represent a User."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
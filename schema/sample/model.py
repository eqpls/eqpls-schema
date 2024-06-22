# -*- coding: utf-8 -*-
'''
Equal Plus
@author: Hye-Churn Jang
'''

#===============================================================================
# Import
#===============================================================================
from typing import List
from pydantic import BaseModel
from common import ID, Key, BaseSchema, ProfSchema, TagSchema, MetaSchema


#===============================================================================
# Implement
#===============================================================================
class User(BaseModel, ProfSchema): pass


class Blog(BaseModel, MetaSchema, TagSchema, BaseSchema):
    title:Key = ''
    text:str = ''
    owner:User
    subscriptions:List[User] = []


class Message(BaseModel, BaseSchema):
    text:str = ''
    owner:User

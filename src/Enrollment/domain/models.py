from __future__ import annotations
from dataclasses import dataclass
from datetime import date, datetime
from sys import getwindowsversion
from typing import AsyncGenerator, List, Optional
from . import commands, events


class Member:

    def __init__(self, id: int, first_name: str, last_name: str, age: str, gender:str, active:str, date_added: datetime, date_edited: datetime):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender 
        self.active = active 
        self.date_added = date_added
        self.date_edited = date_edited
        self.events = []


class Policy:
   def __init__(self, id: int, name: str, start_date: datetime, end_date: datetime, date_added: datetime, date_edited: datetime):
        self.id = id
        self.name = name 
        self.start_date = start_date 
        self.end_date = end_date  
        self.date_added = date_added
        self.date_edited = date_edited
        self.events = []

class Member_Policy:
   def __init__(self, id: int, member_id: int, policy_id: int, is_primary: bool, primary_member_id: int,date_added: datetime, date_edited: datetime):
        self.id = id
        self.member_id = member_id 
        self.policy_id = policy_id 
        self.is_primary = is_primary  
        self.primary_member_id = primary_member_id
        self.date_added = date_added
        self.date_edited = date_edited
        self.events = []

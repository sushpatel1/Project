from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

from .models import Member




class Event(ABC):
    pass


@dataclass
class PolicyUpdated(Event):
    id: int
    name: str
    start_date: str
    end_date: str
    date_edited: str    


@dataclass
class PolicyAdded(Event):
    id: int
    name: str
    start_date: str
    end_date: str
    date_added: str


@dataclass
class MemberAdded(Event):
     id: int
     first_name: str
     last_name: str
     age: str
     gender: str 
     is_primary: str 
     active: str 
     policy_id: str 
     date_added: str

@dataclass
class MemberUpdated(Event):
     id: int
     first_name: str
     last_name: str
     age: str
     gender: str 
     is_primary: str 
     active: str 
     policy_id: str 
     date_edited: str  

@dataclass
class MemberPolicyAdded(Event):
     id: int
     member_id: int
     policy_id: int
     is_primary: str
     primary_member_id: int
     date_added: str


@dataclass
class MemberDeleted(Event):
    member: Member

"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from abc import ABC
from datetime import datetime
from dataclasses import dataclass
from typing import Optional

import requests


class Command(ABC):
    pass


@dataclass
class AddMemberCommand(Command):
     id: int
     first_name: str
     last_name: str
     age: str
     gender: str 
     active: str 
     date_added: str
     date_edited: str

@dataclass
class UpdateMemberCommand(Command):
     id: int
     first_name: str
     last_name: str
     age: str
     gender: str  
     active: str  
     date_added: str
     date_edited: str

@dataclass
class AddPolicyCommand(Command):
     id: int
     name: str
     start_date: str
     end_date: str
     date_added: str
     date_edited: str

@dataclass
class UpdatePolicyCommand(Command):
     id: int
     name: str
     start_date: str
     end_date: str
     date_added: str
     date_edited: str

@dataclass
class AddMemberPolicyCommand(Command):
     id: int
     member_id: int
     policy_id: int
     is_primary: str
     primary_member_id: int
     date_added: str
     date_edited: str

@dataclass
class DeleteMemberCommand(Command):
    id: int

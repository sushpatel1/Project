import threading
import time
import traceback
from datetime import datetime, timezone
from typing import List
from unittest.mock import Mock
import pytest
from Enrollment.domain.models import Member, Policy, Member_Policy
from Enrollment.services import unit_of_work

pytestmark = pytest.mark.usefixtures("mappers")

        
def insert_member(session, first_name: str, last_name: str, age:str, gender:str,active:str, date_added: str, date_edited: str, ):
    session.execute(
        """
        INSERT INTO members (first_name, last_name, age, gender,active, date_added, date_edited) 
        VALUES (:first_name, :last_name, :age, :gender, :active,:date_added, :date_edited)
        """,
        dict(
            first_name=first_name, 
            last_name=last_name,
            age=age,
            gender=gender,
            active=active,
            date_added=date_added,
            date_edited=date_edited,
        ),
    )

def insert_policy(session, name: str, start_date: str, end_date:str, date_added: str, date_edited: str,):
    session.execute(
        """
        INSERT INTO policies (name, start_date, end_date, date_added, date_edited) 
        VALUES (:name, :start_date, :end_date, :date_added, :date_edited)
        """,
        dict(
            name=name, 
            start_date=start_date,
            end_date=end_date,
            date_added=date_added,
            date_edited=date_edited,
        ),
    )

def insert_member_policy(session, member_id: int, policy_id: int, is_primary:str, primary_member_id:int, date_added: str, date_edited: str,):
    session.execute(
        """
        INSERT INTO member_policy (member_id, policy_id, is_primary,primary_member_id, date_added, date_edited) 
        VALUES (:member_id, :policy_id, :is_primary, :primary_member_id,:date_added, :date_edited)
        """,
        dict(
            member_id=member_id, 
            policy_id=policy_id,
            is_primary=is_primary,
            primary_member_id=primary_member_id,
            date_added=date_added,
            date_edited=date_edited,
        ),
    )

def test_can_retreive_member(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
    insert_member(session, f"Test", f"TestLast",f"23",f"M",f"Y", nu.isoformat(), nu.isoformat())
    session.commit()
    member: Member = None

    uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        member = uow.Enrollments._get_member_by_firstName(f"Test")
        assert member.first_name == f"Test"


def test_can_retreive_policy(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
    insert_policy(session, f"Test Policy", f"01-01-2021",f"", nu.isoformat(), nu.isoformat())
    session.commit()
    policy: Policy = None

    uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        member = uow.Enrollments._get_policy_by_Name(f"Test Policy")
        assert member.name == f"Test Policy"

def test_can_retreive_member_policy(sqlite_session_factory):
    session = sqlite_session_factory()
    nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
    insert_member_policy(session, 1, 2,f"Y",1, nu.isoformat(), nu.isoformat())
    session.commit()
    mem_pol: Member_Policy = None

    uow = unit_of_work.SqlAlchemyUnitOfWork(sqlite_session_factory)
    with uow:
        mem_pol = uow.Enrollments._get_member_policy_by_member_Id(1)
        assert mem_pol.policy_id == 2

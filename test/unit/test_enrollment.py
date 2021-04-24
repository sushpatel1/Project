from datetime import date, datetime, timedelta
import random

from Enrollment.domain import events
from Enrollment.domain.models import Bookmark, Member, Member_Policy, Policy

ok_urls = ["http://", "https://"]


def test_new_member_age():
     created: str = datetime.now().isoformat()
     edited: str = created

     member = Member(0,"TestFirst","TestLast","30","F","Y",created,edited)
     assert member.age == 30

def test_member_gender():
     created: str = datetime.now().isoformat()
     edited: str = created

     member = Member(0,"TestFirst","TestLast","25","F","Y",created,edited)

     assert member.gender == "F"


def test_new_policy_is_active():
     created: str = datetime.now().isoformat()
     edited: str = created
     policy = Policy(1,"Test Policy","01-01-2021","", created, edited)

     assert policy.end_date == ""


def test_member_update_time():
    created: str = datetime.now().isoformat()
    edited: str = created
    member = Member(0,"TestFirst","TestLast","25","F","Y",created,edited)

    member.policy_id = 2
    hours_addition = random.randrange(1, 10)
    update_time = datetime.fromisoformat(member.date_edited)
    member.date_edited = (update_time + timedelta(hours=hours_addition)).isoformat()

    assert member.date_added < member.date_edited

def test_member_policy_for_primary():
    created: str = datetime.now().isoformat()
    edited: str = created
    member = Member(1,"TestFirst","TestLast","25","F","Y",created,edited)
    policy = Policy(2,"Test Policy","01-01-2021","", created, edited)
    mem_pol = Member_Policy(1,1,2,"N",1,created,edited)

    assert (mem_pol.primary_member_id == 1 and mem_pol.is_primary == "N") == True

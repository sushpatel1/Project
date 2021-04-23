from datetime import date, datetime, timedelta
import random

from Enrollment.domain import events
from Enrollment.domain.models import Bookmark, Member, Member_Policy, Policy

ok_urls = ["http://", "https://"]


def test_bookmark_title_is_unique():
    pass

def test_new_member_has_policy():
     created: str = datetime.now().isoformat()
     edited: str = created

     member = Member(0,"TestFirst","TestLast","30","F","Y",created,edited)
     assert member.policy_id == 1

def test_policy_member_age():
     created: str = datetime.now().isoformat()
     edited: str = created

     member = Member(0,"TestFirst","TestLast","25","F","Y",created,edited)

     assert (member.age > 18 and member.is_primary == "Y") == True


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
    mem_pol = Member_Policy(1,1,2,"Y",1,created,edited)

    assert (mem_pol.primary_member_id == 1 and mem_pol.is_primary == "Y") == True

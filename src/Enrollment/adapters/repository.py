from abc import ABC, abstractmethod
from datetime import datetime

# making use of type hints: https://docs.python.org/3/library/typing.html
from typing import List, Set

from Enrollment.adapters import orm
from Enrollment.domain.models import Member, Policy, Member_Policy


class AbstractEnrollmentRepository(ABC):
    def __init__(self):
        # seen is in reference to events detected
        self.seen = set()

    def add_member(self, member: Member) -> None:
        # add to repo
        self._add_member(member)
        # add to event list
        self.seen.add(member)

    def update_member(self, member: Member) -> None:
        # add to repo
        self._update_member(member)
        # add to event list
        self.seen.update(member)

    def delete_member(self, member: Member) -> None:
        # add to repo
        self._delete_member(member)
        # add to event list
        self.seen.remove(member)

    def get_member_by_id(self, value: int) -> Member:
        # get from repo
        member: Member = self._get_member_by_id(value)
        if member:
            self.seen.add(member)
        return member   

    def add_Policy(self, policy: Policy) -> None:
        # add to repo
        self._add_policy(policy)
        # add to event list
        self.seen.add(policy)

    def add_member_Policy(self, member_policy: Member_Policy) -> None:
        # add to repo
        self._add_member_policy(member_policy)
        # add to event list
        self.seen.add(member_policy)


    def get_member_policy_by_id(self, value: int) -> Member_Policy:
        # get from repo
        mem_pol: Member_Policy = self._get_member_policy_by_member_Id(value)
        if mem_pol:
            self.seen.add(mem_pol)
        return mem_pol     

    def _get_member_by_firstName(self, value: str) -> Member:
        member: Member = self._get_member_by_firstName(value)
        if member:
            self.seen.add(member)
        return member
    
    def _get_policy_by_Name(self, value: str) -> Policy:
        policy: Policy = self._get_policy_by_Name(value)
        if policy:
            self.seen.add(policy)
        return policy

    def get_policy_by_id(self, value: int) -> Policy:
        # get from repo
        policy: Policy = self._get_policy_by_id(value)
        if policy:
            self.seen.add(policy)
        return policy 

    def update_policy(self, policy: Policy) -> None:
        # add to repo
        self._update_policy(policy)
        # add to event list
        self.seen.update(policy)
   
    @abstractmethod
    def _add_member(self, member: Member) -> None:
        raise NotImplementedError("Derived classes must implement add_one")
    
    @abstractmethod
    def _update_member(self, member: Member) -> None:
        raise NotImplementedError("Derived classes must implement update")
  
    @abstractmethod
    def _delete_member(member: Member) -> None:
        raise NotImplementedError("Derived classes must implement delete")
    
    @abstractmethod
    def _get_member_policy_by_member_Id(self, value: int) -> Member_Policy:
       raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _get_member_by_id(self, value: int) -> Member:
        raise NotImplementedError("Derived classes must implement get")

    @abstractmethod
    def _add_policy(self, policy: Policy) -> None:
        raise NotImplementedError("Derived classes must implement add_one")

    @abstractmethod
    def _get_member_by_firstName(self, value: str) -> Member:
        raise NotImplementedError("Derived classes must implement get")
    
    @abstractmethod
    def _get_policy_by_Name(self, value: str) -> Policy:
        raise NotImplementedError("Derived classes must implement get")
    
    @abstractmethod
    def _add_member_policy(self, member_policy: Member_Policy) -> None:
        raise NotImplementedError("Derived classes must implement add_one")
    
    @abstractmethod
    def _update_policy(self, policy: Policy) -> None:
        raise NotImplementedError("Derived classes must implement update")
  
    @abstractmethod
    def _get_policy_by_id(self, value: int) -> Policy:
        raise NotImplementedError("Derived classes must implement get")



class SqlAlchemyEnrollmentRepository(AbstractEnrollmentRepository):
    """
    Uses guidance from the basic SQLAlchemy 1.4 tutorial: https://docs.sqlalchemy.org/en/14/orm/tutorial.html
    """

    def __init__(self, session) -> None:
        super().__init__()
        self.session = session

    def _add_member(self, member: Member) -> None:
        self.session.add(member)
        # self.session.commit()

    def _update_member(self, member: Member) -> None:
        self.session.update(member)
        self.session.commit()
   
    def _delete_member(self, member: Member) -> None:
        self.seen.delete(member)
        self.session.commit

    def _get_member_policy_by_member_Id(self, value: int) -> Member_Policy:
        answer = self.session.query(Member_Policy).filter(Member_Policy.member_id == value)
        return answer.one()

    def _get_member_by_id(self, value: int) -> Member:
        answer = self.session.query(Member).filter(Member.id == value)
        return answer.one()

    def _add_policy(self, policy: Policy) -> None:
        self.session.add(policy)

    def _add_member_policy(self, member_policy: Member_Policy) -> None:
        self.session.add(member_policy)

    def _get_member_by_firstName(self, value: str) -> Member:
         answer = self.session.query(Member).filter(Member.first_name == value)
         return answer.one()
    
    def _get_policy_by_Name(self, value: str) -> Policy:
         answer = self.session.query(Policy).filter(Policy.name == value)
         return answer.one()


    def _update_policy(self, policy: Policy) -> None:
        self.session.update(policy)
        self.session.commit()
    
    def _get_policy_by_id(self, value: int) -> Policy:
        answer = self.session.query(Policy).filter(Policy.id == value)
        return answer.one()     


class FakeEnrollmentRepository(AbstractEnrollmentRepository):
    """
    Uses a Python list to store "fake" bookmarks: https://www.w3schools.com/python/python_lists.asp
    """

    def __init__(self, members, policies, memberPolicy):
        super().__init__()
        self._members = set(members)
        self._policies = set(policies)
        self._member_policy = set(memberPolicy)


    def _add_member(self, member) -> None:
        self._members.add(member)

    def _update_member(self, member: List[Member]) -> None:
        self._members.update(member)

    def _delete_member(self, member: Member) -> None:
        self._members.remove(member)

    def _get_member_by_id(self, value: int) -> Member:
        return next((b for b in self._members if b.id == value), None)

    def _add_policy(self, policy) -> None:
        self._policies.add(policy)

    def _add_member_policy(self, member_policy) -> None:
        self._member_policy(member_policy)

    def _get_member_by_firstName(self, value: str) -> Member:
        return next((b for b in self._members if b.first_name == value), None)
    
    def _get_policy_by_Name(self, value: str) -> Policy:
        return next((b for b in self._policies if b.name == value), None)

    def _update_policy(self, policy: List[Policy]) -> None:
        self._policies.update(policy)  
        
    def _get_policy_by_id(self, value: int) -> Policy:
        return next((b for b in self._policies if b.id == value), None)

    def _get_member_policy_by_member_Id(self, value: int) -> Member_Policy:
        return next((b for b in self._member_policy if b.member_id == value),None)

    def _update_member(self, member: Member) -> None:
        try:
            idx = self._members.index(member)
            m = self._members[idx]
            with member:
                m.id = member.id
                m.first_name = member.first_name
                m.last_name = member.last_name
                m.age = member.age
                m.gender = member.gender
                m.is_primary = member.is_primary
                m.active = member.active
                m.policy_id = member.policy_id
                m.date_added =datetime.utc.now()
                m.date_edited = datetime.utc.now()
                self._members[idx] = m
        except:
            self._members.append(member)

        return None

    def _update_policy(self, policy: Policy) -> None:
        try:
            idx = self._policies.index(policy)
            p = self._policies[idx]
            with policy:
                p.id = policy.id
                p.name = policy.name
                p.start_date = policy.start_date
                p.end_date = policy.end_date
                p.date_added =datetime.utc.now()
                p.date_edited = datetime.utc.now()
                self._policies[idx] = p
        except:
            self._policies.append(policy)

        return None

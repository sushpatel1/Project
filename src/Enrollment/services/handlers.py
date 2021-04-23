from __future__ import annotations
from dataclasses import asdict
from typing import List, Dict, Callable, Type, TYPE_CHECKING

from Enrollment.domain import commands, events, models

if TYPE_CHECKING:
    from . import unit_of_work

def add_member(
    cmd: commands.AddMemberCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        member = uow.Enrollments._get_member_by_id(value=cmd.id)
        if not member:
            member = models.Member(
                cmd.id, cmd.first_name, cmd.last_name, cmd.age, cmd.gender, cmd.active, cmd.date_added, cmd.date_edited, 
            )
            uow.Enrollments.add_member(member)
        uow.commit()


def update_member(
    cmd: commands.UpdateMemberCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        member = uow.Enrollments._get_member_by_id(value=cmd.id)
        if member:
            member = models.Member(
                 cmd.id,cmd.first_name, cmd.last_name, cmd.age, cmd.gender, cmd.active, cmd.date_added, cmd.date_edited, 
            )
            uow.Enrollments.update_member(member)
        return member

def delete_member(
    cmd: commands.DeleteMemberCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        member = uow.Enrollments._get_member_by_id(value=cmd.id)
        if member:           
            uow.Enrollments.delete_member(member)

def add_policy(
    cmd: commands.AddPolicyCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        policy = uow.Enrollments._get_policy_by_id(value=cmd.id)
        if not policy:
            policy = models.Policy(
                 cmd.id,cmd.name, cmd.start_date, cmd.end_date, cmd.date_added, cmd.date_edited, 
            )
            uow.Enrollments.add_Policy(policy)
        return policy


def update_policy(
    cmd: commands.UpdatePolicyCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        policy = uow.Enrollments._get_policy_by_id(value=cmd.id)
        if policy:
            policy = models.Policy(
                 cmd.id,cmd.name, cmd.start_date, cmd.end_date, cmd.date_added, cmd.date_edited, 
            )
            uow.Enrollments.update_policy(policy)
        return policy


def add_member_policy(
    cmd: commands.AddMemberPolicyCommand,
    uow: unit_of_work.AbstractUnitOfWork,
):
    with uow:
        memberpolicy = models.Member_Policy(
                 cmd.id,cmd.member_id, cmd.policy_id, cmd.end_date, cmd.date_added, cmd.date_edited, 
            )

        uow.Enrollments.add_member_Policy(memberpolicy)
        return memberpolicy





EVENT_HANDLERS = {
    events.MemberAdded: [add_member],
    events.MemberUpdated: [update_member],
    events.MemberDeleted: [delete_member],
    events.PolicyAdded: [add_policy],
    events.PolicyUpdated:[update_policy],
    events.MemberPolicyAdded: [add_member_policy],
}  # type: Dict[Type[events.Event], List[Callable]]

COMMAND_HANDLERS = {
    commands.AddMemberPolicyCommand: add_member,
    commands.UpdateMemberCommand: update_member,
    commands.DeleteMemberCommand: delete_member,
    commands.AddPolicyCommand: add_policy,
    commands.UpdatePolicyCommand: update_policy,
    commands.AddMemberPolicyCommand: add_member_policy,
}  # type: Dict[Type[commands.Command], Callable]

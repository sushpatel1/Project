from __future__ import annotations
from collections import defaultdict
from datetime import date, datetime, timedelta, timezone
from typing import Dict, List
import pytest
from Enrollment import bootstrap
from Enrollment.domain import commands
from Enrollment.services import handlers, unit_of_work
from Enrollment.adapters import repository

from Enrollment.adapters.orm import start_mappers
from Enrollment.services.unit_of_work import FakeUnitOfWork


def boostrap_test_app():
    return bootstrap.bootstrap(start_orm=False, uow=FakeUnitOfWork())


class TestEnrollment:

    def test_add_policy(self):
        bus = boostrap_test_app()
        nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
        # add one
        bus.handle(
            commands.AddPolicyCommand(
                1,
                f"Test Policy",
                f"01-01-2021"
                f"",
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        assert bus.uow.Enrollments._get_policy_by_id(1) is not None
        assert bus.uow.committed

    def test_add_member(self):
        bus = boostrap_test_app()

        nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
        
          # add one
        bus.handle(
            commands.AddPolicyCommand(
                1,
                f"Test Policy",
                f"01-01-2021"
                f"",
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )
        # add one
        bus.handle(
            commands.AddMemberCommand(
                1,
                f"Test",
                f"Test1"
                f"30",
                f"M",
                f"Y",
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        assert bus.uow.Enrollments.get_member_by_id(1) is not None
        assert bus.uow.committed

    def test_update_policy(self):
        bus = boostrap_test_app()
        nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
        # add one
        bus.handle(
            commands.UpdatePolicyCommand(
                1,
                f"Test Policy",
                f"01-01-2021"
                f"12-01-2021",
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        policy = bus.uow.Enrollments.get_policy_by_id(1)
        assert policy.end_date == '12-01-2021'

    def test_update_member(self):
        bus = boostrap_test_app()

        nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)

        # add one
        bus.handle(
            commands.UpdateMemberCommand(
                1,
                f"Test",
                f"Test1"
                f"32",
                f"M",
                f"Y", 
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )
        
        member = bus.uow.Enrollments.get_member_by_id(1) 
        assert member.age == 32

    def test_delete_member(self):
        bus = boostrap_test_app()
        nu: datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
        # add one
        bus.handle(
            commands.AddMemberCommand(
                2,
                f"MemberTest",
                f"Test2"
                f"30",
                f"M",
                f"Y",
                nu.isoformat(), 
                nu.isoformat(), 
            )
        )
        bus.handle(commands.DeleteMemberCommand(2))

        assert len(bus.uow.Enrollments._get_member_by_id(2)) == 0
    
    def test_add_member_policy(self):
        bus = boostrap_test_app()
        nu:datetime = datetime(2021, 3, 31, 0, 0, 0, 0, tzinfo=timezone.utc)
        bus.handle(
            commands.AddMemberCommand(
                3,
                f"MemberTest",
                f"Test2"
                f"30",
                f"M",
                f"Y",
                nu.isoformat(), 
                nu.isoformat(), 
            )
        )

        bus.handle(
            commands.AddPolicyCommand(
                2,
                f"Test Policy",
                f"01-01-2021"
                f"",
                nu.isoformat(),  # date added
                nu.isoformat(),  # date edited
            )
        )

        bus.handle(
            commands.AddMemberPolicyCommand(1,3,2,"Y",3,nu.isoformat(),nu.isoformat(),)
        )        
        assert bus.uow.Enrollments.get_member_policy_by_id(1) is not None
        assert bus.uow.committed
   
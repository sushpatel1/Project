"""
Note: this is significantly refactored to use the Imperative (a.k.a. Classical) Mappings (https://docs.sqlalchemy.org/en/14/orm/mapping_styles.html#imperative-a-k-a-classical-mappings)
That would have been common in 1.3.x and earlier.
"""
import logging
from typing import Text
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
    Text,
    event,
)

from sqlalchemy.orm import  registry, mapper, relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import Boolean

from Enrollment.domain.models import Member, Member_Policy, Policy

mapper_registry = registry()
Base = mapper_registry.generate_base()

logger = logging.getLogger(__name__)
metadata = MetaData()

members = Table(
    "members",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("first_name", String(255), nullable=False),
    Column("last_name", String(255)),
    Column("age", String(255), nullable=False),
    Column("gender", String(255), nullable=False),
    Column("active", String(255), nullable=False),   
    Column("date_added", Text),
    Column("date_edited", Text)
)

policies = Table(
 "policies",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("name", String(255), unique=True, nullable=False),
    Column("start_date", Text, nullable=False),
    Column("end_date", Text),
    Column("date_added", Text),
    Column("date_edited", Text)
)

member_pilicy = Table(
"member_policy",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("member_id", Integer, ForeignKey('members.id'), nullable=False),
    Column("policy_id", Integer, ForeignKey('policies.id'),nullable=False),
    Column("is_primary", Text),
    Column("primary_member_id", Integer,ForeignKey('members.id')),
    Column("date_added", Text),
    Column("date_edited", Text)

)

def start_mappers():    
    logger.info("starting mappers")
    mapper(Member, members)
    mapper(Policy, policies)
    mapper(Member_Policy, member_pilicy)


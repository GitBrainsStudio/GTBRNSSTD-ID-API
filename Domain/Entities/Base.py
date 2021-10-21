from sqlalchemy.orm import declarative_base
from sqlalchemy.sql.schema import Column, ForeignKey, Table

Base = declarative_base()

AccountsRoles = Table('accounts_roles', Base.metadata,
    Column('account_id', ForeignKey('accounts.id')),
    Column('role_id', ForeignKey('roles.id'))
)


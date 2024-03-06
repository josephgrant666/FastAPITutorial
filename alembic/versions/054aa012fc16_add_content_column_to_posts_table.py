"""Add content column to posts table

Revision ID: 054aa012fc16
Revises: a319eefd35e9
Create Date: 2024-03-02 18:01:53.420472

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '054aa012fc16'
down_revision: Union[str, None] = 'a319eefd35e9'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass

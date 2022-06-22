"""add user table

Revision ID: b4ef16464f1b
Revises: 0ec126447864
Create Date: 2022-06-22 16:18:22.559591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4ef16464f1b'
down_revision = '0ec126447864'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                     sa.Column('email', sa.String(), nullable=False),
                     sa.Column('password', sa.String(), nullable=False),
                     sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                     server_default=sa.text('now()') ,nullable=False),
                     sa.PrimaryKeyConstraint('id'),
                     sa.UniqueConstraint('email'))
    pass


def downgrade():
    op.drop_table('users')
    pass

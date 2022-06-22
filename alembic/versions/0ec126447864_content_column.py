"""content column

Revision ID: 0ec126447864
Revises: c4d26371b97d
Create Date: 2022-06-22 16:13:07.720437

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0ec126447864'
down_revision = 'c4d26371b97d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable =False))
    pass


def downgrade():
    op.drop_column('posts','content')
    pass

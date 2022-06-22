"""create posts table

Revision ID: c4d26371b97d
Revises: 
Create Date: 2022-06-22 16:04:04.880162

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c4d26371b97d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts',sa.Column('id', sa.Integer(), nullable =False, primary_key=True),
    sa.Column('title', sa.String(),nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass

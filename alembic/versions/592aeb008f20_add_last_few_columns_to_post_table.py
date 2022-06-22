"""add last few columns to post table

Revision ID: 592aeb008f20
Revises: c93f37b3c548
Create Date: 2022-06-22 16:32:15.347056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '592aeb008f20'
down_revision = 'c93f37b3c548'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('created_at',
                    sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade():
    op.drop_column('posts' 'created_at')
    pass

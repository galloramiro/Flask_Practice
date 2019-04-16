"""empty message

Revision ID: cbb04678b7a4
Revises: 
Create Date: 2019-04-15 22:37:23.886440

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'cbb04678b7a4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'GenData',
        sa.Column('gen', sa.String(50), nullable=False),
        sa.Column('test', sa.String(50), nullable=False),
        sa.Column('tmp', sa.Float, nullable=False),
        sa.Column('update', sa.DateTime, nullable=False, default=datetime.utcnow),
    )

def downgrade():
    pass

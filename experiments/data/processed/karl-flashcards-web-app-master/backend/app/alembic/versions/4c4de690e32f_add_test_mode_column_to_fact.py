"""add test_mode column to fact

Revision ID: 4c4de690e32f
Revises: 57667899ac6f
Create Date: 2021-06-18 17:55:18.970840

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c4de690e32f'
down_revision = '57667899ac6f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('fact', sa.Column('test_mode', sa.SmallInteger(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('fact', 'test_mode')
    # ### end Alembic commands ###
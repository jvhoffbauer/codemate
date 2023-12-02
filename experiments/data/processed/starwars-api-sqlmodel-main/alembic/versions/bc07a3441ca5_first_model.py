"""first model

Revision ID: bc07a3441ca5
Revises: 
Create Date: 2022-07-31 22:50:52.943640

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'bc07a3441ca5'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('specie',
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('designation', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('average_lifespan', sa.Float(), nullable=False),
    sa.Column('average_height', sa.Float(), nullable=False),
    sa.Column('language', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('skin_color', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('character',
    sa.Column('hair_color', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('height', sa.Float(), nullable=False),
    sa.Column('mass', sa.Float(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('skin_color', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('specie_id', sa.Integer(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['specie_id'], ['specie.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('character')
    op.drop_table('specie')
    # ### end Alembic commands ###
"""Setting up Models

Revision ID: a636bb1e002f
Revises: 
Create Date: 2023-04-05 11:53:04.131037

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a636bb1e002f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bakeries',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.Column('updated_at', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('baked_goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('bakery_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.String(), nullable=True),
    sa.Column('updated_at', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['bakery_id'], ['bakeries.id'], name=op.f('fk_baked_goods_bakery_id_bakeries')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('baked_goods')
    op.drop_table('bakeries')
    # ### end Alembic commands ###
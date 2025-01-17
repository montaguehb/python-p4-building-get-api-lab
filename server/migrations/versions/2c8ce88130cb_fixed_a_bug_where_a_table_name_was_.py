"""fixed a bug where a table name was being improperly named

Revision ID: 2c8ce88130cb
Revises: b206df8eaee9
Create Date: 2023-06-14 10:27:29.591757

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2c8ce88130cb'
down_revision = 'b206df8eaee9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('baked_goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('bakery_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bakery_id'], ['bakeries.id'], name=op.f('fk_baked_goods_bakery_id_bakeries')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('bakery.baked_goods')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bakery.baked_goods',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), nullable=True),
    sa.Column('price', sa.INTEGER(), nullable=True),
    sa.Column('bakery_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['bakery_id'], ['bakeries.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('baked_goods')
    # ### end Alembic commands ###

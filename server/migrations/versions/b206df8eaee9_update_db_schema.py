"""update db schema

Revision ID: b206df8eaee9
Revises: a50cde241c4b
Create Date: 2023-06-14 09:57:19.230017

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b206df8eaee9'
down_revision = 'a50cde241c4b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('bakery.baked_goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('bakery_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bakery_id'], ['bakeries.id'], name=op.f('fk_bakery.baked_goods_bakery_id_bakeries')),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('baked_goods')
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('created_at', sa.DateTime(), server_default=sa.text('(CURRENT_TIMESTAMP)'), nullable=True))
        batch_op.add_column(sa.Column('updated_at', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bakeries', schema=None) as batch_op:
        batch_op.drop_column('updated_at')
        batch_op.drop_column('created_at')
        batch_op.drop_column('name')

    op.create_table('baked_goods',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('bakery.baked_goods')
    # ### end Alembic commands ###

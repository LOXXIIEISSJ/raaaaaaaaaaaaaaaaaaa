"""Last active. V2

Revision ID: 121fe295aa5b
Revises: 8fe734c5effb
Create Date: 2023-02-20 02:23:24.314770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '121fe295aa5b'
down_revision = '8fe734c5effb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('last_active', sa.DateTime(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('last_active')

    # ### end Alembic commands ###

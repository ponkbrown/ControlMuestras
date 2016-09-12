"""empty message

Revision ID: f4fa4ae7fefc
Revises: 35db71814511
Create Date: 2016-09-12 10:48:30.065214

"""

# revision identifiers, used by Alembic.
revision = 'f4fa4ae7fefc'
down_revision = '35db71814511'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mascota', sa.Column('new', sa.String(length=20), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('mascota', 'new')
    ### end Alembic commands ###

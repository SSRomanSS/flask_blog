"""Add two new column to User

Revision ID: 5e12ea69ab10
Revises: a89dbfef15cc
Create Date: 2021-03-29 20:46:23.445651

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e12ea69ab10'
down_revision = 'a89dbfef15cc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('about_me', sa.String(length=160), nullable=True))
    op.add_column('users', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'last_seen')
    op.drop_column('users', 'about_me')
    # ### end Alembic commands ###

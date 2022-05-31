"""empty message

Revision ID: fa2fdcb564a1
Revises: 
Create Date: 2022-05-30 15:05:47.675350

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa2fdcb564a1'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('marvel_hero',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('abilities', sa.String(length=255), nullable=False),
    sa.Column('alias', sa.String(length=50), nullable=False),
    sa.Column('height', sa.Unicode(), nullable=True),
    sa.Column('weight', sa.Unicode(), nullable=True),
    sa.Column('gender', sa.String(), nullable=True),
    sa.Column('image', sa.String(length=100), nullable=True),
    sa.Column('eyes', sa.String(length=20), nullable=True),
    sa.Column('hair', sa.String(length=20), nullable=True),
    sa.Column('bio', sa.String(length=255), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.String(length=40), nullable=False),
    sa.Column('username', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=100), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('first_name', sa.String(length=100), nullable=True),
    sa.Column('last_name', sa.String(length=100), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    op.drop_table('marvel_hero')
    # ### end Alembic commands ###
"""empty message

Revision ID: 749462c959c8
Revises: 676579541796
Create Date: 2022-05-30 15:34:03.463107

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '749462c959c8'
down_revision = '676579541796'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('marvel_hero', 'alias',
               existing_type=sa.VARCHAR(length=50),
               nullable=True)
    op.drop_column('marvel_hero', 'eyes')
    op.drop_column('marvel_hero', 'hair')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('marvel_hero', sa.Column('hair', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.add_column('marvel_hero', sa.Column('eyes', sa.VARCHAR(length=20), autoincrement=False, nullable=True))
    op.alter_column('marvel_hero', 'alias',
               existing_type=sa.VARCHAR(length=50),
               nullable=False)
    # ### end Alembic commands ###

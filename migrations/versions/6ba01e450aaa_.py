"""empty message

Revision ID: 6ba01e450aaa
Revises: 5d931cabaaa5
Create Date: 2021-04-24 22:49:50.395206

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '6ba01e450aaa'
down_revision = '5d931cabaaa5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'likes',
               existing_type=mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_bin'),
               type_=sa.JSON(),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('messages', 'likes',
               existing_type=sa.JSON(),
               type_=mysql.LONGTEXT(charset='utf8mb4', collation='utf8mb4_bin'),
               existing_nullable=True)
    # ### end Alembic commands ###

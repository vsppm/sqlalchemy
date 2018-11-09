"""empty message

Revision ID: 4c093f02e763
Revises: a69dd63925f3
Create Date: 2018-11-08 21:48:36.824051

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4c093f02e763'
down_revision = 'a69dd63925f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_user_association', sa.Column('id', sa.Integer(), autoincrement=True, nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_user_association', 'id')
    # ### end Alembic commands ###
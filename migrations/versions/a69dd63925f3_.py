"""empty message

Revision ID: a69dd63925f3
Revises: 
Create Date: 2018-11-08 20:08:31.226770

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a69dd63925f3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tbl_sqlalchemy_project',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('access', sa.String(length=20), nullable=True),
    sa.Column('created_ts', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_ts', sa.DateTime(timezone=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tbl_sqlalchemy_user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('account', sa.String(length=56), nullable=True),
    sa.Column('created_ts', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_ts', sa.DateTime(timezone=True), nullable=True),
    sa.Column('active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project_user_association',
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['tbl_sqlalchemy_project.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['tbl_sqlalchemy_user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_user_association')
    op.drop_table('tbl_sqlalchemy_user')
    op.drop_table('tbl_sqlalchemy_project')
    # ### end Alembic commands ###
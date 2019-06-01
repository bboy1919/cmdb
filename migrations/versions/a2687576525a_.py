"""empty message

Revision ID: a2687576525a
Revises: fdd5a1d3f941
Create Date: 2019-05-29 18:14:46.650713

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a2687576525a'
down_revision = 'fdd5a1d3f941'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'cabinet', 'idc', ['idc_id'], ['id'])
    op.create_foreign_key(None, 'role_o2m_permission', 'permission', ['permission_id'], ['id'])
    op.create_foreign_key(None, 'role_o2m_permission', 'role', ['role_id'], ['id'])
    op.create_foreign_key(None, 'server', 'cabinet', ['cab_id'], ['id'])
    op.drop_column('server', 'check_update_time')
    op.create_foreign_key(None, 'switch', 'cabinet', ['cab_id'], ['id'])
    op.create_foreign_key(None, 'user_o2m_role', 'user', ['u_id'], ['id'])
    op.create_foreign_key(None, 'user_o2m_role', 'role', ['r_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_o2m_role', type_='foreignkey')
    op.drop_constraint(None, 'user_o2m_role', type_='foreignkey')
    op.drop_constraint(None, 'switch', type_='foreignkey')
    op.add_column('server', sa.Column('check_update_time', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'server', type_='foreignkey')
    op.drop_constraint(None, 'role_o2m_permission', type_='foreignkey')
    op.drop_constraint(None, 'role_o2m_permission', type_='foreignkey')
    op.drop_constraint(None, 'cabinet', type_='foreignkey')
    # ### end Alembic commands ###
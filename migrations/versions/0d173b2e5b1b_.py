"""empty message

Revision ID: 0d173b2e5b1b
Revises: f291644ece57
Create Date: 2019-05-29 13:48:53.037824

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d173b2e5b1b'
down_revision = 'f291644ece57'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'cabinet', 'idc', ['idc_id'], ['id'])
    op.create_foreign_key(None, 'role_o2m_permission', 'role', ['role_id'], ['id'])
    op.create_foreign_key(None, 'role_o2m_permission', 'permission', ['permission_id'], ['id'])
    op.add_column('switch', sa.Column('cabi_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'switch', 'cabinet', ['cabi_id'], ['id'])
    op.create_foreign_key(None, 'user_o2m_role', 'role', ['r_id'], ['id'])
    op.create_foreign_key(None, 'user_o2m_role', 'user', ['u_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_o2m_role', type_='foreignkey')
    op.drop_constraint(None, 'user_o2m_role', type_='foreignkey')
    op.drop_constraint(None, 'switch', type_='foreignkey')
    op.drop_column('switch', 'cabi_id')
    op.drop_constraint(None, 'role_o2m_permission', type_='foreignkey')
    op.drop_constraint(None, 'role_o2m_permission', type_='foreignkey')
    op.drop_constraint(None, 'cabinet', type_='foreignkey')
    # ### end Alembic commands ###
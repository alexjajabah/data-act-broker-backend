"""user_id_optional_for_submission

Revision ID: 159caff749a3
Revises: 0c857b50962a
Create Date: 2016-10-18 14:01:34.328634

"""

# revision identifiers, used by Alembic.
revision = '159caff749a3'
down_revision = '0c857b50962a'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('submission', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('submission', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    ### end Alembic commands ###

"""Add file type to flex field

Revision ID: 101a8199cc94
Revises: 684f82692765
Create Date: 2017-02-27 12:17:24.417876

"""

# revision identifiers, used by Alembic.
revision = '101a8199cc94'
down_revision = '684f82692765'
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
    op.add_column('flex_field', sa.Column('file_type_id', sa.Integer(), nullable=True))
    op.add_column('flex_field', sa.Column('file_letter_name', sa.Text(), nullable=True))
    op.execute('UPDATE flex_field SET file_type_id = job.file_type_id FROM job WHERE flex_field.job_id = job.job_id')
    op.execute('UPDATE flex_field SET file_letter_name = file_type.letter_name FROM file_type WHERE flex_field.file_type_id = file_type.file_type_id')
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('flex_field', 'file_letter_name')
    op.drop_column('flex_field', 'file_type_id')
    ### end Alembic commands ###


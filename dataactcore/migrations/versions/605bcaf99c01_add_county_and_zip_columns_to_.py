"""Add county and zip columns to DetachedAwardProcurement table and zip columns to PublishedAwardFinancialAssistance table

Revision ID: 605bcaf99c01
Revises: 0974293b64c3
Create Date: 2017-12-14 12:34:21.808704

"""

# revision identifiers, used by Alembic.
revision = '605bcaf99c01'
down_revision = '0974293b64c3'
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
    op.add_column('detached_award_procurement', sa.Column('legal_entity_county_code', sa.Text(), nullable=True))
    op.add_column('detached_award_procurement', sa.Column('legal_entity_county_name', sa.Text(), nullable=True))
    op.add_column('detached_award_procurement', sa.Column('legal_entity_zip5', sa.Text(), nullable=True))
    op.add_column('detached_award_procurement', sa.Column('legal_entity_zip_last4', sa.Text(), nullable=True))
    op.add_column('detached_award_procurement', sa.Column('place_of_perform_county_co', sa.Text(), nullable=True))
    op.add_column('detached_award_procurement', sa.Column('place_of_performance_zip5', sa.Text(), nullable=True))
    op.add_column('detached_award_procurement', sa.Column('place_of_perform_zip_last4', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('place_of_perfor_state_code', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('place_of_performance_zip5', sa.Text(), nullable=True))
    op.add_column('published_award_financial_assistance', sa.Column('place_of_perform_zip_last4', sa.Text(), nullable=True))
    ### end Alembic commands ###


def downgrade_data_broker():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('published_award_financial_assistance', 'place_of_performance_zip5')
    op.drop_column('published_award_financial_assistance', 'place_of_perform_zip_last4')
    op.drop_column('published_award_financial_assistance', 'place_of_perfor_state_code')
    op.drop_column('detached_award_procurement', 'place_of_performance_zip5')
    op.drop_column('detached_award_procurement', 'place_of_perform_zip_last4')
    op.drop_column('detached_award_procurement', 'place_of_perform_county_co')
    op.drop_column('detached_award_procurement', 'legal_entity_zip_last4')
    op.drop_column('detached_award_procurement', 'legal_entity_zip5')
    op.drop_column('detached_award_procurement', 'legal_entity_county_name')
    op.drop_column('detached_award_procurement', 'legal_entity_county_code')
    ### end Alembic commands ###


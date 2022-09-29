"""added qty to weekly recipe

Revision ID: ab78a20375b0
Revises: b8020ed5cce8
Create Date: 2022-09-29 14:57:28.578498

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ab78a20375b0'
down_revision = 'b8020ed5cce8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weekly__recipe', sa.Column('qty', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('weekly__recipe', 'qty')
    # ### end Alembic commands ###

"""Changed product migrations to remove the unique name in the bank, this made it impossible for another market to register the same product that it would have in another market

Revision ID: 09b594d8f97a
Revises: 5d30ff0ea4b2
Create Date: 2022-02-19 15:01:37.403687

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09b594d8f97a'
down_revision = '5d30ff0ea4b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('products_name_key', 'products', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('products_name_key', 'products', ['name'])
    # ### end Alembic commands ###

"""empty message

Revision ID: 8ff5e40e993f
Revises: b79efc10e5bc
Create Date: 2022-03-22 19:15:33.590684

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8ff5e40e993f'
down_revision = 'b79efc10e5bc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('property_profiles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=80), nullable=True),
    sa.Column('bedrooms', sa.String(length=3), nullable=True),
    sa.Column('bathroom', sa.String(length=3), nullable=True),
    sa.Column('location', sa.String(length=255), nullable=True),
    sa.Column('price', sa.String(length=20), nullable=True),
    sa.Column('type', sa.String(length=10), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('filename', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('property_profiles')
    # ### end Alembic commands ###

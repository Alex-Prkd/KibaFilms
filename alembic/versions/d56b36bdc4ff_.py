"""empty message

Revision ID: d56b36bdc4ff
Revises: 0b18572eb155
Create Date: 2024-06-22 10:01:21.304806

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd56b36bdc4ff'
down_revision: Union[str, None] = '0b18572eb155'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('movie', sa.Column('status_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'movie', 'status', ['status_id'], ['id'])
    op.drop_constraint('status_movie_id_fkey', 'status', type_='foreignkey')
    op.drop_column('status', 'movie_id')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('status', sa.Column('movie_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('status_movie_id_fkey', 'status', 'movie', ['movie_id'], ['id'])
    op.drop_constraint(None, 'movie', type_='foreignkey')
    op.drop_column('movie', 'status_id')
    # ### end Alembic commands ###

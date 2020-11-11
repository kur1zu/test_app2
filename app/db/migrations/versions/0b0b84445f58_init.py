"""init

Revision ID: 0b0b84445f58
Revises: 
Create Date: 2020-11-07 17:58:34.673111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b0b84445f58'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        'owners',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('reputation', sa.Integer(), nullable=True),
        sa.Column('user_type', sa.Text(), nullable=True),
        sa.Column('accept_rate', sa.Text(), nullable=True),
        sa.Column('profile_image', sa.Text(), nullable=True),
        sa.Column('display_name', sa.Text(), nullable=True),
        sa.Column('link', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
    )
    op.create_table(
        'search_types',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('intitle', sa.Text(), nullable=True),
        sa.Column('sort', sa.Text(), nullable=True),
        sa.Column('order', sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint('id'),
        sa.UniqueConstraint('intitle', 'sort', 'order'),
    )
    op.create_table(
        'questions',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('is_answered', sa.Boolean(), nullable=False),
        sa.Column('accepted_answer_id', sa.Integer(), nullable=True),
        sa.Column('view_count', sa.Integer(), nullable=True),
        sa.Column('bounty_amount', sa.DateTime(), nullable=True),
        sa.Column('bounty_closes_date', sa.Integer(), nullable=True),
        sa.Column('answer_count', sa.Integer(), nullable=False),
        sa.Column('score', sa.Integer(), nullable=False),
        sa.Column('last_activity_date', sa.DateTime(), nullable=False),
        sa.Column('creation_date', sa.DateTime(), nullable=False),
        sa.Column('last_edit_date', sa.DateTime(), nullable=True),
        sa.Column('closed_date', sa.DateTime(), nullable=True),
        sa.Column('locked_date', sa.DateTime(), nullable=True),
        sa.Column('protected_date', sa.DateTime(), nullable=True),
        sa.Column('community_owned_date', sa.DateTime(), nullable=True),
        sa.Column('closed_reason', sa.Text(), nullable=True),
        sa.Column('question_id', sa.Integer(), nullable=False),
        sa.Column('content_license', sa.Text(), nullable=True),
        sa.Column('link', sa.Text(), nullable=False),
        sa.Column('title', sa.Text(), nullable=False),
        sa.Column('tags', sa.ARRAY(sa.Text()), nullable=False),
        sa.Column('search_type_id', sa.Integer(), nullable=False),
        sa.Column('owner_id', sa.Integer(), nullable=False),
        sa.Column(
            'creation_at',
            sa.DateTime(),
            server_default=sa.text('now()'),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ['owner_id'], ['owners.id'], ondelete='cascade'
        ),
        sa.ForeignKeyConstraint(
            ['search_type_id'], ['search_types.id'], ondelete='cascade'
        ),
        sa.PrimaryKeyConstraint('id'),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('questions')
    op.drop_table('search_types')
    op.drop_table('owners')
    # ### end Alembic commands ###

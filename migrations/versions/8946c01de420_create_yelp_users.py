"""create yelp users and friends

Revision ID: 8946c01de420
Revises: 
Create Date: 2022-10-23 13:57:56.931588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8946c01de420'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("average_stars", sa.Numeric),
        sa.Column("compliment_cool", sa.Integer),
        sa.Column("compliment_cute", sa.Integer),
        sa.Column("compliment_funny", sa.Integer),
        sa.Column("compliment_hot", sa.Integer),
        sa.Column("compliment_list", sa.Integer),
        sa.Column("compliment_more", sa.Integer),
        sa.Column("compliment_note", sa.Integer),
        sa.Column("compliment_photos", sa.Integer),
        sa.Column("compliment_plain", sa.Integer),
        sa.Column("compliment_profile", sa.Integer),
        sa.Column("compliment_writer", sa.Integer),
        sa.Column("cool", sa.Integer),
        sa.Column("elite", sa.Integer),
        sa.Column("fans", sa.Integer),
        sa.Column("funny", sa.Integer),
        sa.Column("name", sa.Text),
        sa.Column("review_count", sa.Integer),
        sa.Column("useful", sa.Integer),
        sa.Column("user_id", sa.Text, primary_key=True),
        sa.Column("yelping_since", sa.DateTime),
    )
    op.create_table(
        "user_friends",
        sa.Column("user_id", sa.Text, sa.ForeignKey("users.user_id")),
        sa.Column("friend_id", sa.Text, sa.ForeignKey("users.user_id"))
    )


def downgrade() -> None:
    op.drop_table("user_friends")
    op.drop_table("users")

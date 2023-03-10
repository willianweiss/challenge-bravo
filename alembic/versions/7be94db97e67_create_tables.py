import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "7be94db97e67"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "currency_info",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("currency_code", sa.String(), nullable=False),
        sa.Column("rate", sa.Float(), nullable=False),
        sa.Column("backed_by", sa.String(), server_default="USD", nullable=False),
        sa.Column(
            "updated_at",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
        ),
        sa.Column(
            "currency_type", sa.String(), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_currency_info_currency_code"),
        "currency_info",
        ["currency_code"],
        unique=True,
    )


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(
        op.f("ix_currency_info_currency_code"),
        table_name="currency_info",
    )
    op.drop_table("currency_info")

def downgrade() -> None:
    op.drop_table("auth_refresh_token")
    op.drop_table("auth_user")
async def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    configuration = config.get_section(config.config_ini_section)
    configuration["sqlalchemy.url"] = get_url()
    connectable = AsyncEngine(
        engine_from_config(
            configuration, prefix="sqlalchemy.", poolclass=pool.NullPool, future=True
        )
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)
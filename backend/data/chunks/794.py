async def create_user(request: UserCreateIn):
    new_user: ORMUser = await ORMUser.create(**request.dict())
    redis: ArqRedis = await create_pool(settings=redis_settings)
    await redis.enqueue_job(
        "send_message",
        new_user.id,
        "Congratulations! Your account has been created!",
    )
    return User.from_orm(new_user)
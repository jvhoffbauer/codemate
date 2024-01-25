def register_init(app: FastAPI) -> None:
    """
    初始化连接
    :param app:
    :return:
    """

    @app.on_event("startup")
    async def init_connect():
        # 连接redis
        redis_client.init_redis_connect()

        # 初始化 apscheduler
        schedule.init_scheduler()

        db.connect()

    @app.on_event("shutdown")
    async def shutdown_connect():
        """
        关闭
        :return:
        """
        schedule.shutdown()

        if not db.is_closed():
            db.close()
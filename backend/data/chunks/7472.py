    async def init_connect():
        # 连接redis
        redis_client.init_redis_connect()

        # 初始化 apscheduler
        schedule.init_scheduler()

        db.connect()
    @app.on_event("shutdown")
    async def shutdown_connect():
        """
        关闭
        :return:
        """
        schedule.shutdown()

        if not db.is_closed():
            db.close()
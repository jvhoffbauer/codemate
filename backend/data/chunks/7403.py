    def init_scheduler(self) -> None:
        """
        初始化 apscheduler
        :return:
        """
        job_stores = {"default": SQLAlchemyJobStore(url="sqlite:///jobs.sqlite")}
        self._schedule = AsyncIOScheduler(jobstores=job_stores)
        self._schedule.start()
    def __post_init__(self):
        super().__post_init__()
        # 如果td为int,则表示秒数
        self.td = timedelta(seconds=self.td) if isinstance(self.td, int) else self.td
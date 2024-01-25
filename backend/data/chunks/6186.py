@dataclass
class RecentTimeSelectPerm(SelectPerm):
    """最近时间选择数据集"""

    td: Union[int, timedelta] = 60 * 60 * 24 * 7
    time_column: str = "create_time"

    def __post_init__(self):
        super().__post_init__()
        # 如果td为int,则表示秒数
        self.td = timedelta(seconds=self.td) if isinstance(self.td, int) else self.td

    async def _call(self, admin: ModelAdmin, request: Request, sel: Select) -> Select:
        column = getattr(admin.model, self.time_column)
        return sel.where(column > datetime.now() - self.td)
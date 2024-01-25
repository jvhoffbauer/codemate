@dataclass
class FilterSelectPerm(SelectPerm):
    """filter(where)子句选择数据集"""

    filters: list = None

    async def _call(self, admin: ModelAdmin, request: Request, sel: Select) -> Select:
        if not self.filters:
            return sel
        return sel.filter(*self.filters)
@dataclass
class SimpleSelectPerm(SelectPerm):
    """简单列选择数据集"""

    values: Union[List[str], List[int]] = None
    column: str = "status"

    async def _call(self, admin: ModelAdmin, request: Request, sel: Select) -> Select:
        if not self.values:
            return sel
        column = getattr(admin.model, self.column)
        if len(self.values) == 1:
            return sel.where(column == self.values[0])
        return sel.where(column.in_(self.values))
    def where(self, *whereclause: Union[_ColumnExpressionArgument[bool], bool]) -> Self:
        """Return a new `Select` construct with the given expression added to
        its `WHERE` clause, joined to the existing clause via `AND`, if any.
        """
        return super().where(*whereclause)  # type: ignore[arg-type]
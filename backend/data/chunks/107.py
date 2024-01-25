    def having(self, *having: Union[_ColumnExpressionArgument[bool], bool]) -> Self:
        """Return a new `Select` construct with the given expression added to
        its `HAVING` clause, joined to the existing clause via `AND`, if any.
        """
        return super().having(*having)  # type: ignore[arg-type]
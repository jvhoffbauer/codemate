    @deprecated(
        """
        🚨 You probably want to use `session.exec()` instead of `session.query()`.

        `session.exec()` is SQLModel's own short version with increased type
        annotations.

        Or otherwise you might want to use `session.execute()` instead of
        `session.query()`.
        """
    )
    def query(  # type: ignore
        self, *entities: _ColumnsClauseArgument[Any], **kwargs: Any
    ) -> _Query[Any]:
        """
        🚨 You probably want to use `session.exec()` instead of `session.query()`.

        `session.exec()` is SQLModel's own short version with increased type
        annotations.

        Or otherwise you might want to use `session.execute()` instead of
        `session.query()`.
        """
        return super().query(*entities, **kwargs)
    @deprecated(
        """
        🚨 You should not access `obj._calculate_keys()` directly.

        It is only useful for Pydantic v1.X, you should probably upgrade to
        Pydantic v2.X.
        """,
        category=None,
    )
    def _calculate_keys(
        self,
        include: Optional[Mapping[Union[int, str], Any]],
        exclude: Optional[Mapping[Union[int, str], Any]],
        exclude_unset: bool,
        update: Optional[Dict[str, Any]] = None,
    ) -> Optional[AbstractSet[str]]:
        return _calculate_keys(
            self,
            include=include,
            exclude=exclude,
            exclude_unset=exclude_unset,
            update=update,
        )
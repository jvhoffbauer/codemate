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
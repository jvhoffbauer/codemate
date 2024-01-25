    def _calculate_keys(
        self: "SQLModel",
        include: Optional[Mapping[Union[int, str], Any]],
        exclude: Optional[Mapping[Union[int, str], Any]],
        exclude_unset: bool,
        update: Optional[Dict[str, Any]] = None,
    ) -> Optional[AbstractSet[str]]:
        if include is None and exclude is None and not exclude_unset:
            # Original in Pydantic:
            # return None
            # Updated to not return SQLAlchemy attributes
            # Do not include relationships as that would easily lead to infinite
            # recursion, or traversing the whole database
            return (
                self.__fields__.keys()  # noqa
            )  # | self.__sqlmodel_relationships__.keys()

        keys: AbstractSet[str]
        if exclude_unset:
            keys = self.__fields_set__.copy()  # noqa
        else:
            # Original in Pydantic:
            # keys = self.__dict__.keys()
            # Updated to not return SQLAlchemy attributes
            # Do not include relationships as that would easily lead to infinite
            # recursion, or traversing the whole database
            keys = (
                self.__fields__.keys()  # noqa
            )  # | self.__sqlmodel_relationships__.keys()
        if include is not None:
            keys &= include.keys()

        if update:
            keys -= update.keys()

        if exclude:
            keys -= {k for k, v in exclude.items() if ValueItems.is_true(v)}

        return keys
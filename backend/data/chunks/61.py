    def sqlmodel_init(*, self: "SQLModel", data: Dict[str, Any]) -> None:
        old_dict = self.__dict__.copy()
        if not is_table_model_class(self.__class__):
            self.__pydantic_validator__.validate_python(
                data,
                self_instance=self,
            )
        else:
            sqlmodel_table_construct(
                self_instance=self,
                values=data,
            )
        object.__setattr__(
            self,
            "__dict__",
            {**old_dict, **self.__dict__},
        )
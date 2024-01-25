    def filter_modelfield(
        self,
        fields: Iterable[Union[SqlaField, Any]],
        save_class: Tuple[Union[type, Tuple[Any, ...]], ...] = (ModelField,),
        exclude: Iterable[str] = None,
    ) -> List[ModelField]:
        exclude = exclude or []
        # Filter out any non-model fields from the read fields
        fields = self.filter_insfield(fields, save_class=save_class)
        modelfields = [self.get_modelfield(ins, clone=True) for ins in fields]
        # Filter out any None values or out excluded fields
        modelfields = [
            field for field in modelfields if field and field.name not in exclude
        ]
        return modelfields
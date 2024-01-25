    def filter_insfield(
        self,
        fields: Iterable[Union[SqlaField, Any]],
        save_class: Tuple[Union[type, Tuple[Any, ...]], ...] = None,
        exclude_property: Tuple[Union[type, Tuple[Any, ...]], ...] = (
            RelationshipProperty,
        ),
    ) -> List[Union[InstrumentedAttribute, Any]]:
        result = []
        for field in fields:
            insfield = self.get_insfield(field)
            if insfield is not None:
                if isinstance(insfield.property, exclude_property):
                    continue
            elif save_class and isinstance(field, save_class):
                insfield = field
            if insfield is not None:
                result.append(insfield)
        return sorted(set(result), key=result.index)  # 去重复并保持原顺序
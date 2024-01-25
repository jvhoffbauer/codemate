    def cloned_field(self):
        modelfield = create_cloned_field(self.__dict__["_modelfield"])
        if PYDANTIC_V2:
            kwargs = self.__dict__["_update"]
            name = kwargs.pop("name", modelfield.name)
            alias = kwargs.get("alias", None)
            if alias:
                kwargs.setdefault("validation_alias", alias)
                kwargs.setdefault("serialization_alias", alias)
            field_info = FieldInfo.merge_field_infos(modelfield.field_info, **kwargs)
            field_info.annotation = modelfield.field_info.annotation
            return ModelField(field_info=field_info, name=name, mode=modelfield.mode)
        for k, v in self.__dict__["_update"].items():
            setattr(modelfield, k, v)
        return modelfield
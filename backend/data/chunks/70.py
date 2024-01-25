    def get_type_from_field(field: Any) -> Any:
        if isinstance(field.type_, type) and field.shape == SHAPE_SINGLETON:
            return field.type_
        raise ValueError(f"The field {field.name} has no matching SQLAlchemy type")
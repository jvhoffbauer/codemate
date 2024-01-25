    def get_relationship_to(
        name: str,
        rel_info: "RelationshipInfo",
        annotation: Any,
    ) -> Any:
        origin = get_origin(annotation)
        use_annotation = annotation
        # Direct relationships (e.g. 'Team' or Team) have None as an origin
        if origin is None:
            if isinstance(use_annotation, ForwardRef):
                use_annotation = use_annotation.__forward_arg__
            else:
                return use_annotation
        # If Union (e.g. Optional), get the real field
        elif _is_union_type(origin):
            use_annotation = get_args(annotation)
            if len(use_annotation) > 2:
                raise ValueError(
                    "Cannot have a (non-optional) union as a SQLAlchemy field"
                )
            arg1, arg2 = use_annotation
            if arg1 is NoneType and arg2 is not NoneType:
                use_annotation = arg2
            elif arg2 is NoneType and arg1 is not NoneType:
                use_annotation = arg1
            else:
                raise ValueError(
                    "Cannot have a Union of None and None as a SQLAlchemy field"
                )

        # If a list, then also get the real field
        elif origin is list:
            use_annotation = get_args(annotation)[0]

        return get_relationship_to(
            name=name, rel_info=rel_info, annotation=use_annotation
        )
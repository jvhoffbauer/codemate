    def get_annotations(class_dict: Dict[str, Any]) -> Dict[str, Any]:
        return resolve_annotations(  # type: ignore[no-any-return]
            class_dict.get("__annotations__", {}),
            class_dict.get("__module__", None),
        )
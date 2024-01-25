    def get_annotations(class_dict: Dict[str, Any]) -> Dict[str, Any]:
        return class_dict.get("__annotations__", {})
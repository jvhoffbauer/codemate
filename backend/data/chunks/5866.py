    def update_item(self, obj: TableModelT, values: Dict[str, Any]) -> None:
        """update schema_update data to database,support relational attributes"""
        for k, v in values.items():
            field = get_modelfield_by_alias(self.model, k)
            if not field and not hasattr(obj, k):
                continue
            name = field.name if field else k
            if isinstance(v, dict):
                # Relational attributes, nested;such as: setattr(article.content, "body", "new body")
                sub = getattr(obj, name)
                if not isinstance(sub, dict):  # Ensure that the attribute is an object.
                    self.update_item(sub, v)
                    continue
            setattr(obj, name, v)
    def get_page_schema_child(
        self, unique_id: str
    ) -> Union[Tuple[PageSchemaAdminT, "AdminGroup"], Tuple[None, None]]:
        for child in self._children:
            if child.unique_id == unique_id:
                return child, self
            if isinstance(child, AdminGroup):
                child, parent = child.get_page_schema_child(unique_id)
                if child:
                    return child, parent
        return None, None
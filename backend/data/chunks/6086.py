    def remove_child(self, unique_id: str) -> None:
        self._children = [
            admin for admin in self._children if admin.unique_id != unique_id
        ]
        for admin in self._children:
            if isinstance(admin, AdminGroup):
                admin.remove_child(unique_id)
    def delete_item(self, obj: TableModelT) -> None:
        """delete database data"""
        object_session(obj).delete(obj)
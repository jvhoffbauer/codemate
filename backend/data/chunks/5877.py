    def _delete_items(self, session: Session, item_id: List[str]) -> List[TableModelT]:
        items = self._fetch_item_scalars(session, item_id)
        for item in items:
            self.delete_item(item)
        return items
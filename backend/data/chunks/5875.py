    def _update_items(
        self, session: Session, item_id: List[str], values: Dict[str, Any]
    ) -> List[TableModelT]:
        items = self._fetch_item_scalars(session, item_id)
        for item in items:
            self.update_item(item, values)
        return items
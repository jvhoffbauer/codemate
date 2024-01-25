    def _read_items(self, session: Session, item_id: List[str]) -> List[SchemaReadT]:
        items = self._fetch_item_scalars(session, item_id)
        return [self.read_item(obj) for obj in items]
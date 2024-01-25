    def _create_items(
        self, session: Session, items: List[Dict[str, Any]]
    ) -> List[TableModelT]:
        if not items:
            return []
        objs = [self.create_item(item) for item in items]
        session.add_all(objs)
        session.flush()
        return objs
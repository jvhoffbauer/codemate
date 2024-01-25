    def _fetch_item_scalars(
        self, session: Session, item_id: Iterable[str]
    ) -> List[TableModelT]:
        sel = select(self.model).where(
            self.pk.in_(list(map(get_python_type_parse(self.pk), item_id)))
        )
        return session.scalars(sel).all()
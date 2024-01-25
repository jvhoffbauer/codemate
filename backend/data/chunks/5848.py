    def _calc_ordering(self, orderBy, orderDir):
        sqlfield = self._select_entities.get(
            orderBy, self._filter_entities.get(orderBy)
        )
        order = None
        if sqlfield is not None:
            order = sqlfield.desc() if orderDir == "desc" else sqlfield.asc()
            return [order]
        elif self.ordering is not None:
            order = self.parser.filter_insfield(
                self.ordering,
                save_class=(
                    UnaryExpression,
                    Label,
                ),
            )
        return order
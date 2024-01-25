    def calc_filter_clause(self, data: Dict[str, Any]) -> List[BinaryExpression]:
        lst = []
        for k, v in data.items():
            sqlfield = self._filter_entities.get(k)
            if sqlfield is not None:
                operator, val = self._parser_query_value(
                    v, python_type_parse=get_python_type_parse(sqlfield)
                )
                if operator:
                    lst.append(getattr(sqlfield, operator)(*val))
        return lst
    @staticmethod
    def _parser_query_value(
        value: Any, operator: str = "__eq__", python_type_parse: Callable = str
    ) -> Tuple[Optional[str], Union[tuple, None]]:
        if isinstance(value, str):
            if not value:
                return None, None
            match = sql_operator_pattern.match(value)
            if match:
                op_key = match.group(1)
                operator = sql_operator_map.get(op_key)
                value = value.replace(f"[{op_key}]", "")
                if not value:
                    return None, None
                if operator in ["like", "not_like"] and value.find("%") == -1:
                    return operator, (f"%{value}%",)
                elif operator in ["in_", "not_in"]:
                    return operator, (
                        list(map(python_type_parse, set(value.split(",")))),
                    )
                elif operator == "between":
                    value = value.split(",")[:2]
                    if len(value) < 2:
                        return None, None
                    return operator, tuple(map(python_type_parse, value))
        return operator, (python_type_parse(value),)
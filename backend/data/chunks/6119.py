    def get_field_amis_table_column_type(self, type_: Type) -> dict:
        """Get amis table column type from pydantic model field type."""
        kwargs = {}
        type_ = annotation_outer_type(type_)
        if type_ in {str, Any}:
            pass
        elif issubclass(type_, bool):
            kwargs["type"] = "switch"
            kwargs["disabled"] = True
            kwargs["filterable"] = {
                "options": [
                    {"label": _("YES"), "value": True},
                    {"label": _("NO"), "value": False},
                ]
            }
        elif issubclass(type_, datetime.datetime):
            kwargs["type"] = "datetime"
        elif issubclass(type_, datetime.date):
            kwargs["type"] = "date"
        elif issubclass(type_, datetime.time):
            kwargs["type"] = "time"
        elif issubclass(type_, Enum):
            items = (
                type_.choices
                if issubclass(type_, Choices)
                else [(m.value, m.value) for m in type_]
            )
            kwargs["type"] = "mapping"
            kwargs["filterable"] = {
                "options": [{"label": v, "value": k} for k, v in items]
            }
            kwargs["map"] = {
                k: f"<span class='label label-{label.value}'>{v}</span>"
                for (k, v), label in zip(items, cyclic_generator(LabelEnum))
            }
        elif issubclass(type_, (dict, Json)):
            kwargs["type"] = "json"
        elif field_annotation_is_scalar_sequence(type_):
            kwargs["type"] = "each"
            kwargs["items"] = {
                "type": "tpl",
                "tpl": "<span class='label label-info m-l-sm'><%= this.item %></span>",
            }
        return kwargs
    def get_field_amis_form_item_type(
        self, type_: Any, is_filter: bool, required: bool = False
    ) -> dict:
        """Get amis form item type from pydantic model field type."""
        kwargs = {}
        type_ = annotation_outer_type(type_)
        if type_ in {str, Any}:
            kwargs["type"] = "input-text"
        elif issubclass(type_, Enum):
            items = (
                type_.choices
                if issubclass(type_, Choices)
                else [(m.value, m.value) for m in type_]
            )
            kwargs.update(
                {
                    "type": "select",
                    "options": [{"label": label, "value": v} for v, label in items],
                    "extractValue": True,
                    "joinValues": False,
                }
            )
            if not required or is_filter:
                kwargs["clearable"] = True
        elif issubclass(type_, bool):
            kwargs["type"] = "switch"
        elif is_filter:
            if issubclass(type_, datetime.datetime):
                kwargs["type"] = "input-datetime-range"
                kwargs["format"] = "YYYY-MM-DD HH:mm:ss"
                # 给筛选的 DateTimeRange 添加 today 标签
                kwargs[
                    "ranges"
                ] = "today,yesterday,7daysago,prevweek,thismonth,prevmonth,prevquarter"
            elif issubclass(type_, datetime.date):
                kwargs["type"] = "input-date-range"
                kwargs["format"] = "YYYY-MM-DD"
            elif issubclass(type_, datetime.time):
                kwargs["type"] = "input-time-range"
                kwargs["format"] = "HH:mm:ss"
            else:
                kwargs["type"] = "input-text"
        elif issubclass(type_, int):
            kwargs["type"] = "input-number"
            kwargs["precision"] = 0
            kwargs["validations"] = Validation(isInt=True).amis_dict()
        elif issubclass(type_, float):
            kwargs["type"] = "input-number"
            kwargs["precision"] = 3
            kwargs["validations"] = Validation(isFloat=True).amis_dict()
        elif issubclass(type_, datetime.datetime):
            kwargs["type"] = "input-datetime"
            kwargs["format"] = "YYYY-MM-DD HH:mm:ss"
        elif issubclass(type_, datetime.date):
            kwargs["type"] = "input-date"
            kwargs["format"] = "YYYY-MM-DD"
        elif issubclass(type_, datetime.time):
            kwargs["type"] = "input-time"
            kwargs["format"] = "HH:mm:ss"
        elif issubclass(type_, (dict, Json)):
            kwargs["type"] = "json-editor"
        elif issubclass(type_, BaseModel):
            # pydantic model parse to InputSubForm
            kwargs["type"] = "input-sub-form"
            kwargs["labelField"] = get_model_label_field_name(type_)
            kwargs["btnLabel"] = model_config_attr(type_, "title", None)
            kwargs["form"] = self.as_amis_form(type_, is_filter=is_filter).amis_dict()
        else:
            kwargs["type"] = "input-text"
        if kwargs.get("type") == "input-text":
            kwargs["clearable"] = True
            kwargs["clearValueOnEmpty"] = True
        return kwargs
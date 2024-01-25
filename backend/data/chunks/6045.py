    async def get_column_quick_edit(
        self, request: Request, modelfield: ModelField
    ) -> Optional[Dict[str, Any]]:
        item = await self.get_form_item(request, modelfield, action=CrudEnum.update)
        if not isinstance(item, (dict, BaseModel)):
            return None
        if isinstance(item, BaseModel):
            item = item.dict(
                exclude_none=True, by_alias=True, exclude={"name", "label"}
            )
        item.update({"saveImmediately": True})
        if item.get("type") == "switch":
            item.update({"mode": "inline"})
        return item
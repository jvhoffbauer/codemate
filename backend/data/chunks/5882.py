    async def on_update_pre(
        self,
        request: Request,
        obj: SchemaUpdateT,
        item_id: Union[List[str], List[int]],
        **kwargs,
    ) -> Dict[str, Any]:
        data = obj.dict(exclude=self.update_exclude, exclude_unset=True, by_alias=True)
        data = {
            key: val
            for key, val in data.items()
            if val is not None or field_allow_none(model_fields(self.model)[key])
        }
        return data
        async def depend(
            item_id: ItemIdListDepend,
            sel: self.AnnotatedSelect,  # type: ignore
        ):
            item_id = list(map(get_python_type_parse(self.pk), item_id))
            filtered_id = await self.db.async_scalars(
                sel.where(self.pk.in_(item_id)).with_only_columns(self.pk)
            )
            return filtered_id.all()
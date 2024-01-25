    def bind_model_admin(
        cls, pk_admin: "ModelAdmin", insfield: InstrumentedAttribute
    ) -> Optional["LinkModelForm"]:
        if not isinstance(insfield.property, RelationshipProperty):
            return None
        table = insfield.property.secondary
        if table is None:
            return None
        admin = None
        link_key = None
        item_key = None
        for key in table.foreign_keys:
            if (
                key.column.table != pk_admin.model.__table__
            ):  # Get the associated third-party table
                admin = pk_admin.app.site.get_model_admin(key.column.table.name)
                link_key = key
            else:
                item_key = key
        if admin and link_key and item_key:
            admin.link_models[pk_admin.model.__table__.name] = (
                table,
                link_key.parent,
                item_key.parent,
            )
            return LinkModelForm(
                pk_admin=pk_admin,
                display_admin=admin,
                link_model=table,
                link_col=link_key.parent,
                item_col=item_key.parent,
            )
        return None
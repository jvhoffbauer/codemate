    def registered_admin_actions(self) -> Dict[str, "AdminAction"]:
        admin_actions = {
            "create": AdminAction(
                admin=self,
                name="create",
                label=_("Create"),
                flags=["toolbar"],
                getter=lambda request: self.get_create_action(request, bulk=False),
            ),
            "update": AdminAction(
                admin=self,
                name="update",
                tooltip=_("Update"),
                flags=["item"],
                getter=lambda request: self.get_update_action(request, bulk=False),
            ),
            "delete": AdminAction(
                admin=self,
                name="delete",
                action=ActionType.Ajax(
                    icon="fa fa-times text-danger",
                    tooltip=_("Delete"),
                    confirmText=_("Are you sure you want to delete row ${%s}?")
                    % self.pk_name,
                    api=f"delete:{self.router_path}/item/${self.pk_name}",
                ),
                flags=["item"],
            ),
            "bulk_delete": AdminAction(
                admin=self,
                name="bulk_delete",
                action=ActionType.Ajax(
                    label=_("Bulk Delete"),
                    confirmText=_("Are you sure you want to delete the selected rows?"),
                    api=f"delete:{self.router_path}/item/" + "${ids|raw}",
                ),
                flags=["bulk"],
            ),
        }
        if self.enable_bulk_create:
            admin_actions["bulk_create"] = AdminAction(
                admin=self,
                name="bulk_create",
                label=_("Bulk Create"),
                flags=["toolbar"],
                getter=lambda request: self.get_create_action(request, bulk=True),
            )
        if self.schema_read:
            admin_actions["read"] = AdminAction(
                admin=self,
                name="read",
                label=_("View"),
                flags=["item"],
                getter=lambda request: self.get_read_action(request),
            )
        if self.bulk_update_fields:
            admin_actions["bulk_update"] = AdminAction(
                admin=self,
                name="bulk_update",
                label=_("Bulk Update"),
                flags=["bulk"],
                getter=lambda request: self.get_update_action(request, bulk=True),
            )
        for maker in self.admin_action_maker:
            admin_action = maker(self)
            admin_actions[admin_action.name] = admin_action
        return admin_actions
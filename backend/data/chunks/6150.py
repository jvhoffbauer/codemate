    def registered_admin_actions(self) -> Dict[str, "AdminAction"]:
        actions = super().registered_admin_actions
        return {
            key: action
            for key, action in actions.items()
            if key
            not in {
                "create",
                "update",
                "delete",
                "bulk_delete",
                "bulk_update",
                "bulk_create",
            }
        }
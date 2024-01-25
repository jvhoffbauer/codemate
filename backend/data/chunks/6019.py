    @cached_property
    def registered_admin_actions(self) -> Dict[str, "AdminAction"]:
        admin_actions = {}
        for maker in self.admin_action_maker:
            admin_action = maker(self)
            if admin_action:
                admin_actions[admin_action.name] = admin_action
        return admin_actions
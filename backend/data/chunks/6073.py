    def __init__(
        self,
        admin: BaseActionAdmin,
        *,
        name: str = None,
        label: str = None,
        action: Action = None,
        flags: Union[str, List[str]] = None,
        getter: Callable[[Request], ActionT] = None,
        **kwargs,
    ):
        self.admin = admin
        assert self.admin, "admin is None"
        self.action = action or self.action.copy()
        self.action = self.action.update_from_dict(kwargs)
        self.name = name or self.action.id or self.action.name
        assert self.name, "name is None"
        self.label = label or self.action.label or self.action.tooltip
        assert self.label, "label is None"
        self.flags = flags or ["item"]
        if isinstance(self.flags, str):
            self.flags = [self.flags]
        self.getter = getter
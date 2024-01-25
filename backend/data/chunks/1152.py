    def __init__(
        self, security_scheme: SecurityBase, scopes: Optional[Sequence[str]] = None
    ):
        self.security_scheme = security_scheme
        self.scopes = scopes
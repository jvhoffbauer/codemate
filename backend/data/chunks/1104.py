    def __init__(
        self,
        scopes: Annotated[
            Optional[List[str]],
            Doc(
                """
                This will be filled by FastAPI.
                """
            ),
        ] = None,
    ):
        self.scopes: Annotated[
            List[str],
            Doc(
                """
                The list of all the scopes required by dependencies.
                """
            ),
        ] = (
            scopes or []
        )
        self.scope_str: Annotated[
            str,
            Doc(
                """
                All the scopes required by all the dependencies in a single string
                separated by spaces, as defined in the OAuth2 specification.
                """
            ),
        ] = " ".join(self.scopes)
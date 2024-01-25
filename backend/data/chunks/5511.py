    def __post_init__(self):
        """Post Init."""
        if self.width and self.height:
            self.max_size = None
    def __hash__(self):
        return hash(self.entrypoint_route.path)
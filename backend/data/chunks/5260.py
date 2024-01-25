    def reset(self) -> None:
        for _name, var in self._vars.items():
            var.set(None)
@dataclass
class SelectPerm:
    name: str
    label: str
    reverse: bool = False
    call: SelectPermCallable = None

    def __post_init__(self):
        if self.call is None and hasattr(self, "_call"):
            self.call = self._call
        assert self.call is not None, "call must be set"
@dataclass
class ObjectWithUpdateWrapper:
    obj: Any
    update: Dict[str, Any]

    def __getattribute__(self, __name: str) -> Any:
        if __name in self.update:
            return self.update[__name]
        return getattr(self.obj, __name)
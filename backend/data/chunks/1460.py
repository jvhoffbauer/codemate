@dataclass
class Item:
    name: str
    description: Union[str, None] = None
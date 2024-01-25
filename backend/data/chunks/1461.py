@dataclass
class Author:
    name: str
    items: List[Item] = field(default_factory=list)  # (3)
@dataclass
class Item:
    name: str
    date: datetime
    price: Optional[float] = None
    owner_ids: Optional[List[int]] = None
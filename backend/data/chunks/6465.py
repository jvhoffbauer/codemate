    @validator("timeline")
    @classmethod
    def sort_timeline(cls, value):
        """Sort the timeline history before inserting into the model"""
        return dict(sorted(value.items()))
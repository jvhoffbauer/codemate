    def latest(self):
        """Get latest available history value."""
        return list(self.timeline.values())[-1] if self.timeline else 0
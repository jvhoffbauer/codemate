    def isoformat(self):
        return datetime.datetime.strptime(self.date, self.strformat).isoformat()
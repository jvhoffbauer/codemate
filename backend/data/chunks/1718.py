    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()
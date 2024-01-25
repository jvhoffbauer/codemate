    def _load_local_model(self):
        self.model = joblib.load(self.path)
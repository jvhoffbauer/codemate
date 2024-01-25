    def __init__(self, app: "AdminApp"):
        super().__init__(app)
        self.file_directory = self.file_directory or self.file_path
        os.makedirs(self.file_directory, exist_ok=True)
        self.static_path = self.mount_staticfile()
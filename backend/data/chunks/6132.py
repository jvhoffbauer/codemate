    def mount_staticfile(self) -> str:
        self.site.fastapi.mount(
            self.file_path,
            StaticFiles(directory=self.file_directory),
            self.file_directory,
        )
        return self.site.router_path + self.file_path
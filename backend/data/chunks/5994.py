    def unique_id(self) -> str:
        unique_str = f"{self.__class__.__module__}:{self.__class__.__qualname__}"
        if self.app is not self:
            unique_str += f"{self.app.unique_id}"
        return md5_hex(unique_str)[:16]
    @cached_property
    def read_permission_fields(self) -> Dict[str, str]:
        """读取权限字段"""
        return self.get_permission_fields("read")
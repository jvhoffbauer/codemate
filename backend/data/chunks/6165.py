    @cached_property
    def update_permission_fields(self) -> Dict[str, str]:
        """更新权限字段"""
        return self.get_permission_fields("update")
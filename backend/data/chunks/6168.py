    def list_permission_fields(self) -> Dict[str, str]:
        """列表权限字段"""
        return self.get_permission_fields("list")
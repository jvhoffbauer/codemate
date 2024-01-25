    def filter_permission_fields(self) -> Dict[str, str]:
        """过滤筛选权限字段"""
        return self.get_permission_fields("filter")
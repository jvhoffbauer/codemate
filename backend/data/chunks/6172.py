    async def get_deny_fields(self, request: Request, action: str = None) -> Set[str]:
        """获取没有权限的字段"""
        cache_key = f"{self.unique_id}_exclude_fields"
        request_cache = request.scope.get(cache_key, {})
        if action in request_cache:
            return request_cache[action]
        check_fields = {}
        if action == "list":
            check_fields = self.list_permission_fields.keys()
        elif action == "filter":
            check_fields = self.filter_permission_fields.keys()
        elif action == "create":
            check_fields = self.create_permission_fields.keys()
        elif action == "update":
            check_fields = self.update_permission_fields.keys()
        elif action == "read":
            check_fields = self.read_permission_fields.keys()
        else:
            pass
        fields = {
            field
            for field in check_fields
            if not await self.has_field_permission(request, field, action)
        }
        request_cache[action] = fields
        if cache_key not in request.scope:
            request.scope[cache_key] = request_cache
        return fields
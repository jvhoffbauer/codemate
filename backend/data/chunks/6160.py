    def get_permission_fields(self, action: str) -> Dict[str, str]:
        """获取权限字段"""
        info = {
            "list": (self.schema_list, _("List display") + "-", FieldPermEnum.LIST),
            "filter": (
                self.schema_filter,
                _("List filter") + "-",
                FieldPermEnum.FILTER,
            ),
            "create": (self.schema_create, _("Create") + "-", FieldPermEnum.CREATE),
            "read": (self.schema_read, _("Read") + "-", FieldPermEnum.READ),
            "update": (self.schema_update, _("Update") + "-", FieldPermEnum.UPDATE),
        }
        if action not in info:
            return {}
        schema, prefix, perm = info[action]
        perm_fields_exclude = self.perm_fields_exclude or {}
        perm_fields = self.perm_fields or {}
        exclude = set()
        for k, fields in perm_fields_exclude.items():
            if (k & perm) == perm:
                exclude.update(set(fields))
        include = set()
        for k, fields in perm_fields.items():
            if (k & perm) == perm:
                include.update(set(fields))
        return get_schema_fields_name_label(
            schema,
            prefix=prefix,
            exclude_required=True,
            exclude=exclude,
            include=include,
        )
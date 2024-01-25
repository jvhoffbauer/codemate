def is_superuser(user: UserInDB):
    return RoleEnum.superuser.value in utils.ensure_enums_to_strs(
        user.admin_roles or []
    )
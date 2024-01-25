def read_roles(current_user: UserInDB = Depends(get_current_active_superuser)):
    """
    Retrieve roles.
    """
    roles = crud.utils.ensure_enums_to_strs(RoleEnum)
    return {"roles": roles}
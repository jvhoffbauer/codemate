@router.get("/user/info", summary="获取用户信息", name="获取用户信息", description="此API没有验证权限")
def get_user_info(*, current_user: User = Depends(deps.get_current_user)) -> Any:
    """
    获取用户信息 这个路由分组没有验证权限
    :param current_user:
    :return:
    """
    return resp.ok(data=model_to_dict(current_user))
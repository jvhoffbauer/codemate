def get_all_user_info(
    page: int = Query(1),  # 分页等通用字段可以提取出来封装
    page_size: int = Query(20),
):
    user, pagination = User().fetch_all(page=page, page_size=page_size)

    return resp.ok(data=user, pagination=pagination)
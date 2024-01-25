def items_test(*, bar: str = Query(..., title="测试字段", description="测试字段描述")) -> Any:
    """
    用户登录
    :param bar:
    :param db:
    :return:
    """
    # 测试redis使用
    redis_client.set("test_items", bar, ex=60)
    redis_test = redis_client.get("test_items")

    return resp.ok(data=redis_test)
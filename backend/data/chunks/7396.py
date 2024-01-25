def params_match(full_name_k1: str, key2: str):
    """
    去掉url ?后面的参数 只取路径
    :param full_name_k1:
    :param key2:
    :return:
    """
    key1 = full_name_k1.split("?")[0]
    return util.key_match2(key1, key2)
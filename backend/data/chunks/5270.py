def path_to_cls_name(path):
    return snake_convert(path[1:].replace("/", "_"))
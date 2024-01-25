def snake_convert(s):
    if not isinstance(s, str):
        return s
    components = s.split("_")
    return "".join(x.title() for x in components)
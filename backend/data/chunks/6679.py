def rename_if_scope_child_component(owner: type, child, postfix: str):
    if is_scope_child(owner, child):
        child = component_name(f"{owner.__name__}.{postfix}", owner.__module__)(child)
    return child
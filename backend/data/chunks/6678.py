def is_scope_child(owner: type, child: type):
    return (
        (
            owner.__dict__.get(child.__name__) is child
            or owner.__dict__.get(child.__name__) is Optional[child]
        )
        and child.__qualname__ == owner.__qualname__ + "." + child.__name__
        and child.__module__ == owner.__module__
    )
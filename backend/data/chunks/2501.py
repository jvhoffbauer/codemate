async def asyncgen_state_try(state: Dict[str, str] = Depends(get_state)):
    state["/async_raise"] = "asyncgen raise started"
    try:
        yield state["/async_raise"]
    except AsyncDependencyError:
        errors.append("/async_raise")
    finally:
        state["/async_raise"] = "asyncgen raise finalized"
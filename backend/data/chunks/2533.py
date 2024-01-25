def get_sync_async_raise_other(state: str = Depends(asyncgen_state_try)):
    assert state == "asyncgen raise started"
    raise OtherDependencyError()
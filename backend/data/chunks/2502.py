def generator_state_try(state: Dict[str, str] = Depends(get_state)):
    state["/sync_raise"] = "generator raise started"
    try:
        yield state["/sync_raise"]
    except SyncDependencyError:
        errors.append("/sync_raise")
    finally:
        state["/sync_raise"] = "generator raise finalized"
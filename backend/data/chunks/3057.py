@app.get("/user", dependencies=[Depends(set_up_request_state_dependency)])
def get_user():
    request_state = legacy_request_state_context_var.get()
    assert request_state
    return request_state["user"]
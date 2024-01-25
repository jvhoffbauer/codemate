def test_dependency_contextvars():
    """
    Check that custom middlewares don't affect the contextvar context for dependencies.

    The code before yield and the code after yield should be run in the same contextvar
    context, so that request_state_context_var.reset(contextvar_token).

    If they are run in a different context, that raises an error.
    """
    response = client.get("/user")
    assert response.json() == "deadpond"
    assert response.headers["custom"] == "foo"
@needs_py310
def test_query_params_str_validations_no_query():
    client = get_client()
    response = client.get("/items/")
    assert response.status_code == 200
    assert response.json() == "Hello World"
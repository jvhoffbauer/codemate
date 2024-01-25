@needs_py310
def test_query_params_str_validations_q_fixedquery():
    client = get_client()
    response = client.get("/items/", params={"q": "fixedquery"})
    assert response.status_code == 200
    assert response.json() == "Hello fixedquery"
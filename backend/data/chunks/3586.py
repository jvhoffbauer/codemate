def test_no_body_status_code_exception_handlers():
    response = client.get("/http-no-body-statuscode-exception")
    assert response.status_code == 204
    assert not response.content
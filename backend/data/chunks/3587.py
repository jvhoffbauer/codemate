def test_no_body_status_code_with_detail_exception_handlers():
    response = client.get("/http-no-body-statuscode-with-detail-exception")
    assert response.status_code == 204
    assert not response.content
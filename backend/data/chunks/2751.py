def test_required_nonable_body_embed_no_content():
    response = client.post("/body-embed")
    assert response.status_code == 422
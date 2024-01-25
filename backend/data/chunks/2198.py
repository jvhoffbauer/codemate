def test_get():
    response = client.post(
        "/invoices/", json={"id": "fooinvoice", "customer": "John", "total": 5.3}
    )
    assert response.status_code == 200, response.text
    assert response.json() == {"msg": "Invoice received"}
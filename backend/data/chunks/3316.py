def test_decimal_encoder_int():
    data = {"value": Decimal(2)}
    assert jsonable_encoder(data) == {"value": 2}
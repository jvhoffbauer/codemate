def test_decimal_encoder_float():
    data = {"value": Decimal(1.23)}
    assert jsonable_encoder(data) == {"value": 1.23}
def test_encode_custom_json_encoders_model_pydanticv1():
    class ModelWithCustomEncoder(BaseModel):
        dt_field: datetime

        class Config:
            json_encoders = {
                datetime: lambda dt: dt.replace(
                    microsecond=0, tzinfo=timezone.utc
                ).isoformat()
            }

    class ModelWithCustomEncoderSubclass(ModelWithCustomEncoder):
        class Config:
            pass

    model = ModelWithCustomEncoder(dt_field=datetime(2019, 1, 1, 8))
    assert jsonable_encoder(model) == {"dt_field": "2019-01-01T08:00:00+00:00"}
    subclass_model = ModelWithCustomEncoderSubclass(dt_field=datetime(2019, 1, 1, 8))
    assert jsonable_encoder(subclass_model) == {"dt_field": "2019-01-01T08:00:00+00:00"}
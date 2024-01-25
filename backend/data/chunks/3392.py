        @field_serializer("dt_field")
        def serialize_datetime(self, dt_field: datetime):
            return dt_field.replace(microsecond=0, tzinfo=timezone.utc).isoformat()
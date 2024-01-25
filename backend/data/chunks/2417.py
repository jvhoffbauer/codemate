        @field_serializer("a_uuid")
        def serialize_a_uuid(self, v):
            return str(v)
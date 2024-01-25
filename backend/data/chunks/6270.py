    def test_scalar_type_datetime(self):
        from datetime import datetime

        assert annotation_outer_type(datetime) == datetime
        def check_string_keys(map):
            for key, value in map.items:
                assert isinstance(key, str)
                if isinstance(value, dict):
                    check_string_keys(value)
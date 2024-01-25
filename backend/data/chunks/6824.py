        def _openapi_compatible(value: dict):
            assert (
                packaging.version.parse(value["openapi"]) in supported_openapi_versions
            )
            value["openapi"] = ANY
            return value
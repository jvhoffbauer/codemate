@pytest.fixture
def openapi_compatible():
    supported_openapi_versions = [
        packaging.version.parse("3.0.2"),
        packaging.version.parse("3.1.0"),
    ]

    if packaging.version.parse(pydantic.VERSION) >= packaging.version.parse("1.10.0"):

        def _openapi_compatible(value: dict):
            assert (
                packaging.version.parse(value["openapi"]) in supported_openapi_versions
            )
            value["openapi"] = ANY
            return value

    else:

        def _openapi_compatible(obj: dict):
            for k, v in obj.items():
                if isinstance(v, dict):
                    obj[k] = _openapi_compatible(obj[k])
            if "const" in obj and "default" in obj:
                del obj["default"]

            assert packaging.version.parse(obj["openapi"]) in supported_openapi_versions
            obj["openapi"] = ANY

            return obj

    return _openapi_compatible
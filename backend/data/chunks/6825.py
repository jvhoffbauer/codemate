        def _openapi_compatible(obj: dict):
            for k, v in obj.items():
                if isinstance(v, dict):
                    obj[k] = _openapi_compatible(obj[k])
            if "const" in obj and "default" in obj:
                del obj["default"]

            assert packaging.version.parse(obj["openapi"]) in supported_openapi_versions
            obj["openapi"] = ANY

            return obj
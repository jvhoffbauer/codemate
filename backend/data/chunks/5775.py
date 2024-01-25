    def _read(*args: Any, **kwargs: Any) -> MosaicJSON:
        """Match signature of `cogeo_mosaic.backends.BaseBackend._read`"""
        data = read_json_fixture(fname)
        for qk in data["tiles"]:
            data["tiles"][qk] = [
                os.path.join(os.path.dirname(fname), f) for f in data["tiles"][qk]
            ]
        return MosaicJSON(**data)
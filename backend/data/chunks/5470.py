        def available_bands(
            src_path=Depends(self.path_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Return a list of supported bands."""
            with rasterio.Env(**env):
                with self.reader(src_path, **reader_params) as src_dst:
                    return src_dst.bands
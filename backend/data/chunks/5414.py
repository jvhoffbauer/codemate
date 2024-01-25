        def bounds(
            src_path=Depends(self.path_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Return the bounds of the COG."""
            with rasterio.Env(**env):
                with self.reader(src_path, **reader_params) as src_dst:
                    return {"bounds": src_dst.geographic_bounds}
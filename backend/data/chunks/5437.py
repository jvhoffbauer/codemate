    def point(self):
        """Register /point endpoints."""

        @self.router.get(
            r"/point/{lon},{lat}",
            response_model=Point,
            response_class=JSONResponse,
            responses={200: {"description": "Return a value for a point"}},
        )
        def point(
            lon: float = Path(..., description="Longitude"),
            lat: float = Path(..., description="Latitude"),
            src_path=Depends(self.path_dependency),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Get Point value for a dataset."""
            with rasterio.Env(**env):
                with self.reader(src_path, **reader_params) as src_dst:
                    pts = src_dst.point(
                        lon,
                        lat,
                        **layer_params,
                        **dataset_params,
                    )

            return {
                "coordinates": [lon, lat],
                "values": pts.data.tolist(),
                "band_names": pts.band_names,
            }
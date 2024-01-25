        @self.router.get(
            r"/{lng},{lat}/assets",
            responses={200: {"description": "Return list of COGs"}},
        )
        def assets_for_lon_lat(
            src_path=Depends(self.path_dependency),
            lng: float = Query(None, description="Longitude"),
            lat: float = Query(None, description="Latitude"),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Return a list of assets which overlap a point"""
            with rasterio.Env(**env):
                with self.reader(
                    src_path,
                    reader=self.dataset_reader,
                    reader_options={**reader_params},
                    **backend_params,
                ) as src_dst:
                    return src_dst.assets_for_point(lng, lat)
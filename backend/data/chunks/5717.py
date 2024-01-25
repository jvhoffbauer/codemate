    def assets(self):
        """Register /assets endpoint."""

        @self.router.get(
            r"/{minx},{miny},{maxx},{maxy}/assets",
            responses={200: {"description": "Return list of COGs in bounding box"}},
        )
        def assets_for_bbox(
            src_path=Depends(self.path_dependency),
            minx: float = Query(None, description="Left side of bounding box"),
            miny: float = Query(None, description="Bottom of bounding box"),
            maxx: float = Query(None, description="Right side of bounding box"),
            maxy: float = Query(None, description="Top of bounding box"),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Return a list of assets which overlap a bounding box"""
            with rasterio.Env(**env):
                with self.reader(
                    src_path,
                    reader=self.dataset_reader,
                    reader_options={**reader_params},
                    **backend_params,
                ) as src_dst:
                    return src_dst.assets_for_bbox(minx, miny, maxx, maxy)

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

        @self.router.get(
            r"/{z}/{x}/{y}/assets",
            responses={200: {"description": "Return list of COGs"}},
        )
        def assets_for_tile(
            z: int = Path(..., ge=0, le=30, description="Mercator tiles's zoom level"),
            x: int = Path(..., description="Mercator tiles's column"),
            y: int = Path(..., description="Mercator tiles's row"),
            src_path=Depends(self.path_dependency),
            backend_params=Depends(self.backend_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Return a list of assets which overlap a given tile"""
            with rasterio.Env(**env):
                with self.reader(
                    src_path,
                    reader=self.dataset_reader,
                    reader_options={**reader_params},
                    **backend_params,
                ) as src_dst:
                    return src_dst.assets_for_tile(x, y, z)
        @self.router.get(
            "/info",
            response_model=MultiBaseInfo,
            response_model_exclude_none=True,
            response_class=JSONResponse,
            responses={
                200: {
                    "description": "Return dataset's basic info or the list of available assets."
                }
            },
        )
        def info(
            src_path=Depends(self.path_dependency),
            asset_params=Depends(self.assets_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Return dataset's basic info or the list of available assets."""
            with rasterio.Env(**env):
                with self.reader(src_path, **reader_params) as src_dst:
                    return src_dst.info(**asset_params)
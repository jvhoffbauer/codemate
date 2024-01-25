        @self.router.get(
            "/statistics",
            response_class=JSONResponse,
            response_model=Statistics,
            responses={
                200: {
                    "content": {"application/json": {}},
                    "description": "Return dataset's statistics.",
                }
            },
        )
        def statistics(
            src_path=Depends(self.path_dependency),
            layer_params=Depends(self.layer_dependency),
            dataset_params=Depends(self.dataset_dependency),
            image_params=Depends(self.img_dependency),
            stats_params=Depends(self.stats_dependency),
            histogram_params=Depends(self.histogram_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Get Dataset statistics."""
            with rasterio.Env(**env):
                with self.reader(src_path, **reader_params) as src_dst:
                    return src_dst.statistics(
                        **layer_params,
                        **image_params,
                        **dataset_params,
                        **stats_params,
                        hist_options={**histogram_params},
                    )
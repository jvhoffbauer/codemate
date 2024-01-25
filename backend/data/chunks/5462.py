        def geojson_statistics(
            geojson: Union[FeatureCollection, Feature] = Body(
                ..., description="GeoJSON Feature or FeatureCollection."
            ),
            src_path=Depends(self.path_dependency),
            layer_params=Depends(AssetsBidxExprParamsOptional),
            dataset_params=Depends(self.dataset_dependency),
            image_params=Depends(self.img_dependency),
            stats_params=Depends(self.stats_dependency),
            histogram_params=Depends(self.histogram_dependency),
            reader_params=Depends(self.reader_dependency),
            env=Depends(self.environment_dependency),
        ):
            """Get Statistics from a geojson feature or featureCollection."""
            fc = geojson
            if isinstance(fc, Feature):
                fc = FeatureCollection(features=[geojson])

            with rasterio.Env(**env):
                with self.reader(src_path, **reader_params) as src_dst:
                    # Default to all available assets
                    if not layer_params.assets and not layer_params.expression:
                        layer_params.assets = src_dst.assets

                    for feature in fc:
                        data = src_dst.feature(
                            feature.dict(exclude_none=True),
                            **layer_params,
                            **image_params,
                            **dataset_params,
                        )

                        stats = get_array_statistics(
                            data.as_masked(),
                            **stats_params,
                            **histogram_params,
                        )

                    feature.properties = feature.properties or {}
                    feature.properties.update(
                        {
                            # NOTE: because we use `src_dst.feature` the statistics will be in form of
                            # `Dict[str, BandStatistics]` and not `Dict[str, Dict[str, BandStatistics]]`
                            "statistics": {
                                f"{data.band_names[ix]}": BandStatistics(**stats[ix])
                                for ix in range(len(stats))
                            }
                        }
                    )

            return fc.features[0] if isinstance(geojson, Feature) else fc
                def _reader(src_path: str):
                    with rasterio.Env(**env):
                        with factory.reader(src_path, **reader_params) as src_dst:
                            return src_dst.part(
                                bbox,
                                width=width,
                                height=height,
                                dst_crs=crs,
                                bounds_crs=crs,
                                **layer_params,
                                **dataset_params,
                            )
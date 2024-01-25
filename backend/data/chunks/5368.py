        @factory.router.get("/stac", response_model=Item, name="Create STAC Item")
        def create_stac(
            src_path: str = Depends(factory.path_dependency),
            datetime: Optional[str] = Query(
                None,
                description="The date and time of the assets, in UTC (e.g 2020-01-01, 2020-01-01T01:01:01).",
            ),
            extensions: Optional[List[str]] = Query(
                None, description="STAC extension URL the Item implements."
            ),
            collection: Optional[str] = Query(
                None, description="The Collection ID that this item belongs to."
            ),
            collection_url: Optional[str] = Query(
                None, description="Link to the STAC Collection."
            ),
            # properties: Optional[Dict] = Query(None, description="Additional properties to add in the item."),
            id: Optional[str] = Query(
                None,
                description="Id to assign to the item (default to the source basename).",
            ),
            asset_name: Optional[str] = Query(
                "data", description="asset name for the source (default to 'data')."
            ),
            asset_roles: Optional[List[str]] = Query(
                None, description="list of asset's roles."
            ),
            asset_media_type: Literal[tuple(media)] = Query(  # type: ignore
                "auto", description="Asset's media type"
            ),
            asset_href: Optional[str] = Query(
                None, description="Asset's URI (default to source's path)"
            ),
            with_proj: bool = Query(
                True, description="Add the `projection` extension and properties."
            ),
            with_raster: bool = Query(
                True, description="Add the `raster` extension and properties."
            ),
            with_eo: bool = Query(
                True, description="Add the `eo` extension and properties."
            ),
            max_size: Optional[int] = Query(
                1024,
                gt=0,
                description="Limit array size from which to get the raster statistics.",
            ),
        ):
            """Create STAC item."""
            properties = (
                {}
            )  # or properties = properties or {} if we add properties in Query

            dt = None
            if datetime:
                if "/" in datetime:
                    start_datetime, end_datetime = datetime.split("/")
                    properties["start_datetime"] = datetime_to_str(
                        str_to_datetime(start_datetime)
                    )
                    properties["end_datetime"] = datetime_to_str(
                        str_to_datetime(end_datetime)
                    )
                else:
                    dt = str_to_datetime(datetime)

            return create_stac_item(
                src_path,
                input_datetime=dt,
                extensions=extensions,
                collection=collection,
                collection_url=collection_url,
                properties=properties,
                id=id,
                asset_name=asset_name,
                asset_roles=asset_roles,
                asset_media_type=asset_media_type,
                asset_href=asset_href or src_path,
                with_proj=with_proj,
                with_raster=with_raster,
                with_eo=with_eo,
                raster_max_size=max_size,
            ).to_dict()
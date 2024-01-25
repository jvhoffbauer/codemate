        async def TileMatrixSet_info(
            TileMatrixSetId: Literal[tuple(self.supported_tms.list())] = Path(
                ..., description="TileMatrixSet Name."
            )
        ):
            """
            OGC Specification: http://docs.opengeospatial.org/per/19-069.html#_tilematrixset
            """
            return self.supported_tms.get(TileMatrixSetId)
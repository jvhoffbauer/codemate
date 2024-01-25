def PixelSelectionParams(
    pixel_selection: PixelSelectionMethod = Query(
        PixelSelectionMethod.first,
        description="Pixel selection method.",
    )
) -> MosaicMethodBase:
    """
    Returns the mosaic method used to combine datasets together.
    """
    return pixel_selection.method()
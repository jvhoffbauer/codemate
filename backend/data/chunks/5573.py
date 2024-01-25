def ColorMapParams(
    colormap_name: ColorMapName = Query(None, description="Colormap name"),
) -> Optional[Dict]:
    """Colormap Dependency."""
    if colormap_name:
        return cmap.get(colormap_name.value)

    return None
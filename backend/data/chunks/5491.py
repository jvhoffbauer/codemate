def ColorMapParams(
    colormap_name: ColorMapName = Query(None, description="Colormap name"),
    colormap: str = Query(None, description="JSON encoded custom Colormap"),
) -> Optional[ColorMapType]:
    """Colormap Dependency."""
    if colormap_name:
        return cmap.get(colormap_name.value)

    if colormap:
        try:
            c = json.loads(
                colormap,
                object_hook=lambda x: {int(k): parse_color(v) for k, v in x.items()},
            )

            # Make sure to match colormap type
            if isinstance(c, Sequence):
                c = [(tuple(inter), parse_color(v)) for (inter, v) in c]

            return c
        except json.JSONDecodeError as e:
            raise HTTPException(
                status_code=400, detail="Could not parse the colormap value."
            ) from e

    return None
def RescalingParams(
    rescale: Optional[List[str]] = Query(
        None,
        title="Min/Max data Rescaling",
        description="comma (',') delimited Min,Max range. Can set multiple time for multiple bands.",
        example=["0,2000", "0,1000", "0,10000"],  # band 1  # band 2  # band 3
    )
) -> Optional[List[Tuple[float, ...]]]:
    """Min/Max data Rescaling"""
    if rescale:
        return [tuple(map(float, r.replace(" ", "").split(","))) for r in rescale]

    return None
@dataclass
class ImageRenderingParams(DefaultDependency):
    """Image Rendering options."""

    add_mask: bool = Query(
        True, alias="return_mask", description="Add mask to the output data."
    )
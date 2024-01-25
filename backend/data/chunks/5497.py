@dataclass
class ExpressionParams(DefaultDependency):
    """Expression parameters."""

    expression: Optional[str] = Query(
        None,
        title="Band Math expression",
        description="rio-tiler's band math expression",
        examples={
            "simple": {"description": "Simple band math.", "value": "b1/b2"},
            "multi-bands": {
                "description": "Semicolon (;) delimited expressions (band1: b1/b2, band2: b2+b3).",
                "value": "b1/b2;b2+b3",
            },
        },
    )
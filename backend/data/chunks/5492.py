def DatasetPathParams(url: str = Query(..., description="Dataset URL")) -> str:
    """Create dataset path from args"""
    return url
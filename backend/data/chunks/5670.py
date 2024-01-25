def CustomPathParams(directory: str = Query(..., description="Give me a url.")) -> str:
    """Custom path Dependency."""
    return directory
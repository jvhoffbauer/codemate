def main(
    req: func.HttpRequest,
    context: func.Context,
) -> func.HttpResponse:
    """Run App in AsgiMiddleware."""
    return func.AsgiMiddleware(app).handle(req, context)
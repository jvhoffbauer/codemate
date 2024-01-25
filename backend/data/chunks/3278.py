@app.post("/", callbacks=callback_router.routes)
def main_route(callback_url: HttpUrl):
    pass  # pragma: no cover
@app.get("/", openapi_extra={"x-custom-extension": "value"})
def route_with_extras():
    return {}
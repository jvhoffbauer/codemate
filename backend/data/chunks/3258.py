@app.get("/server-error")
def route_with_server_error():
    raise RuntimeError("Oops!")
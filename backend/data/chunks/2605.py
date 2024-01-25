@app.post("/tuple-of-models/")
def post_tuple_of_models(square: Tuple[Coordinate, Coordinate]):
    return square
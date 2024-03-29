- Endpoint to retrieve a dictionary containing metadata about all supported algorithms
- Uses FastAPI's `@app.get()` decorator and specifies the endpoint path as '/algorithms'
- Returns a dictionary with keys corresponding to algorithm names and values being their respective metadata objects (obtained using `metadata()`)
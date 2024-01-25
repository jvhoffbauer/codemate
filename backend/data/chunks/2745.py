@app.post("/body-embed")
def send_body_embed(b: Union[str, None] = Body(embed=True)):
    return b
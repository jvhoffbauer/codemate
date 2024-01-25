@app.post("/form/python-tuple")
def post_form_param_tuple(items: tuple = Form()):
    return items
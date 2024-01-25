@app.post("/form/python-set")
def post_form_param_set(items: set = Form()):
    return items
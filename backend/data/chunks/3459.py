@app.post("/form/python-list")
def post_form_param_list(items: list = Form()):
    return items
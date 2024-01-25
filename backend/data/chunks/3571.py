@app.get("/orjson_non_str_keys")
def get_orjson_non_str_keys():
    key = quoted_name(value="msg", quote=False)
    return {key: "Hello World", 1: 1}
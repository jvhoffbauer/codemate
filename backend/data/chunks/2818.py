def response_model_list_of_model_no_annotation():
    return [
        DBUser(name="John", surname="Doe", password_hash="secret"),
        DBUser(name="Jane", surname="Does", password_hash="secret2"),
    ]
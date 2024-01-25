def no_response_model_annotation_forward_ref_list_of_model() -> "List[User]":
    return [
        DBUser(name="John", surname="Doe", password_hash="secret"),
        DBUser(name="Jane", surname="Does", password_hash="secret2"),
    ]
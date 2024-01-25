def get_allowed_username(username):
    chars_to_remove = '()<>@,;:"/\[]?={}'
    modified_username = username
    for char in chars_to_remove:
        modified_username = modified_username.replace(char, "-")
    return modified_username
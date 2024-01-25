def get_user_by_email(email: str):
    return models.User.filter(models.User.email == email).first()
def get_user(user_id: int):
    return models.User.filter(models.User.id == user_id).first()
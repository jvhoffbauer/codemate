def get_users(skip: int = 0, limit: int = 100):
    return list(models.User.select().offset(skip).limit(limit))
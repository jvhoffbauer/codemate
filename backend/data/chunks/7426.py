    @classmethod
    def fetch_all(cls, page: int = 1, page_size: int = 10):
        db = User.undelete().select(
            User.name,
            User.email,
            User.phone,
            User.username,
            User.avatar,
            User.created_at,
            User.deleted_at,
        )

        user_list, paginate = paginator(db, page, page_size, "id desc")

        return user_list, paginate
    @classmethod
    def single_by_id(cls, uid: int):
        db = (
            User.undelete()
            .select(
                User.id, User.name, User.email, User.phone, User.username, User.avatar
            )
            .where(User.id == uid)
        )
        return db.first()
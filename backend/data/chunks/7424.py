    @classmethod
    def single_by_phone(cls, phone: int = 0):
        db = User.select()

        if phone != 0:
            db = db.where(User.phone == phone)
        return db.first()
        # if db:
        #     return model_to_dict(db)
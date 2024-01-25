    def update(self, db: Session, *, db_obj: User, obj_in: UserUpdate) -> User:
        if obj_in.password:
            hashed_password = get_password_hash(obj_in.password)
            obj_in = UserUpdateHashedPassword(
                **obj_in.dict(exclude_unset=True), hashed_password=hashed_password
            )
        return super().update(db, db_obj=db_obj, obj_in=obj_in)
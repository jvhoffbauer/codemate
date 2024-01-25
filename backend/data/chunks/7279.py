    def create(self, db: Session, obj_in: UserCreate | UserAdminCreate) -> User:
        data = jsonable_encoder(obj_in)
        data["hashed_password"] = get_password_hash(obj_in.password)
        del data["password"]
        db_obj = User(**data)
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
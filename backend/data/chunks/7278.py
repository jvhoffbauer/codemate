    def get_by_email(self, db: Session, email: EmailStr) -> User | None:
        return db.query(User).filter(User.email == email).first()
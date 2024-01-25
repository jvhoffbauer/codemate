    def authenticate(
        self, db: Session, *, email: EmailStr, password: str
    ) -> User | None:
        user = self.get_by_email(db, email=email)
        if not user:
            return None
        if not verify_password(
            plain_password=password, hashed_password=user.hashed_password
        ):
            return None
        return user
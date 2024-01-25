    def get_multi(
        self, db: Session, *, skip: int = 0, limit: int = 100
    ) -> list[ModelType]:
        limit = min(500, limit)  # don't allow for arbitrarily large queries
        return db.query(self.model).offset(skip).limit(limit).all()
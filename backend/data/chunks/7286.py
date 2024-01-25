    def update(
        self, db: Session, *, db_obj: ModelType, obj_in: UpdateSchemaType
    ) -> ModelType:
        update_data = obj_in.dict(exclude_unset=True)
        for field in update_data:
            if hasattr(db_obj, field):
                setattr(db_obj, field, update_data[field])
            else:
                raise AttributeError(
                    f"{self.model.__name__} does't have field '{field}'"
                )
        db.add(db_obj)
        db.commit()
        db.refresh(db_obj)
        return db_obj
    def undelete(cls):
        # for logic delete
        return cls.select().where(SQL("deleted_at is NULL"))
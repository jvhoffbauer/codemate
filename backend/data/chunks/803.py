@generic_repr
class Base(db.Model):
    __abstract__ = True
    created_on = db.Column(
        db.DateTime, default=datetime.utcnow, server_default=db.func.now()
    )
    updated_on = db.Column(
        db.DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow,
        server_default=db.func.now(),
    )
    id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    def __init__(__pydantic_self__, **data: Any) -> None:
        # Uses something other than `self` the first arg to allow "self" as a
        # settable attribute

        # SQLAlchemy does very dark black magic and modifies the __init__ method in
        # sqlalchemy.orm.instrumentation._generate_init()
        # so, to make SQLAlchemy work, it's needed to explicitly call __init__ to
        # trigger all the SQLAlchemy logic, it doesn't work using cls.__new__, setting
        # attributes obj.__dict__, etc. The __init__ method has to be called. But
        # there are cases where calling all the default logic is not ideal, e.g.
        # when calling Model.model_validate(), as the validation is done outside
        # of instance creation.
        # At the same time, __init__ is what users would normally call, by creating
        # a new instance, which should have validation and all the default logic.
        # So, to be able to set up the internal SQLAlchemy logic alone without
        # executing the rest, and support things like Model.model_validate(), we
        # use a contextvar to know if we should execute everything.
        if finish_init.get():
            sqlmodel_init(self=__pydantic_self__, data=data)
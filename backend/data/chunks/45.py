@contextmanager
def partial_init() -> Generator[None, None, None]:
    token = finish_init.set(False)
    yield
    finish_init.reset(token)
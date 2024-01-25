def probe(ep):
    @ep.method()
    def probe() -> str:
        raise ZeroDivisionError

    @ep.method()
    def probe2() -> str:
        raise RuntimeError

    return ep
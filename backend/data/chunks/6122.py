def cyclic_generator(iterable: Iterable[_T]) -> Generator[_T, None, None]:
    while True:
        yield from iterable
def check_calls(calls: List[List[Union[str, Dict[str, Any]]]]):
    assert calls[0][0] == {
        "name": "Deadpond",
        "secret_name": "Dive Wilson",
        "age": None,
        "id": 1,
    }
    assert calls[1][0] == {
        "name": "Spider-Boy",
        "secret_name": "Pedro Parqueador",
        "age": None,
        "id": 2,
    }
    assert calls[2][0] == {
        "name": "Rusty-Man",
        "secret_name": "Tommy Sharp",
        "age": 48,
        "id": 3,
    }
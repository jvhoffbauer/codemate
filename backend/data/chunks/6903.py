@pytest.fixture
def ep(ep):
    @ep.method()
    def probe(whole_params: WholeParams = Params(...)) -> List[int]:
        return [int(item) + whole_params.amount for item in whole_params.data]

    return ep
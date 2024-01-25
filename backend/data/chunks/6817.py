@pytest.fixture(params=[False, True])
def add_path_postfix(request):
    return request.param
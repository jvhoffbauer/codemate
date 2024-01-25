def test_component_name_isolated_by_their_path(pytester, api_package):
    """Test we can mix methods with same names in one openapi.json schema"""

    pytester.makepyfile(
        """
import pytest
import fastapi_jsonrpc as jsonrpc


# override conftest.py `app` fixture
@pytest.fixture
def app():
    from api.web import api_v1 as api_v1_web
    from api.mobile import api_v1 as api_v1_mobile

    app = jsonrpc.API()
    app.bind_entrypoint(api_v1_web)
    app.bind_entrypoint(api_v1_mobile)
    return app


def test_no_collide(app_client):
    resp = app_client.get('/openapi.json')
    resp_json = resp.json()

    paths = resp_json['paths']
    schemas = resp_json['components']['schemas']

    for path in (
        '/api/v1/mobile/jsonrpc/probe',
        '/api/v1/web/jsonrpc/probe',
    ):
        assert path in paths

    # Response model the same and deduplicated
    assert '_Response[probe]' in schemas

    if '_Params[probe]' not in schemas:
        for component_name in (
            'api__mobile___Params[probe]',
            'api__mobile___Request[probe]',
            'api__web___Params[probe]',
            'api__web___Request[probe]',
        ):
            assert component_name in schemas
"""
    )

    # force reload module to drop component cache
    # it's more efficient than use pytest.runpytest_subprocess()
    sys.modules.pop("fastapi_jsonrpc")

    result = pytester.runpytest_inprocess()
    result.assert_outcomes(passed=1)
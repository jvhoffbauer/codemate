def api_package(request, pytester):
    """Create package with structure
        api \
            mobile.py
            web.py

    mobile.py and web.py has similar content except entrypoint path
    """

    # Re-use our infrastructure layer
    try:
        pytester.copy_example("tests/conftest.py")
    except LookupError:
        pytester.copy_example("conftest.py")

    # Create api/web.py and api/mobile.py files with same methods
    entrypoint_tpl = """
from fastapi import Body
from typing import List


import fastapi_jsonrpc as jsonrpc

api_v1 = jsonrpc.Entrypoint(
    '{ep_path}',
)

@api_v1.method()
def probe(
    {unique_param_name}: List[str] = Body(..., examples=['111', '222']),
    amount: int = Body(..., gt=5, examples=[10]),
) -> List[int]:
    return [1, 2, 3]
"""

    if request.param == "uniq-sig":
        mobile_param_name = "mobile_data"
        web_param_name = "web_data"
    else:
        assert request.param == "same-sig"
        mobile_param_name = web_param_name = "data"

    api_dir = pytester.mkpydir("api")
    mobile_py = api_dir.joinpath("mobile.py")
    mobile_py.write_text(
        entrypoint_tpl.format(
            ep_path="/api/v1/mobile/jsonrpc",
            unique_param_name=mobile_param_name,
        ),
    )

    web_py = api_dir.joinpath("web.py")
    web_py.write_text(
        entrypoint_tpl.format(
            ep_path="/api/v1/web/jsonrpc",
            unique_param_name=web_param_name,
        ),
    )
    return api_dir
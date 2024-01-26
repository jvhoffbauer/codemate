- Registers two API routes for a page using FastAPI's `Router`.
- The first route is for GET requests and returns an HTML response with no schema included (`include_in_schema=False`). It also requires a permission dependency (`self.page_permission_depend`) and has custom keyword arguments passed to it through `**self.page_route_kwargs`.
- The second route is for POST requests and returns a BaseAmisApiOut model as output. It also requires the same permission dependency and has a similar set of options as the GET route, including support for JSON parsing based on the value of `self.page_parser_mode`.
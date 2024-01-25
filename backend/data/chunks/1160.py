def get_graphql_response(
    *,
    settings: Settings,
    query: str,
    after: Union[str, None] = None,
    category_id: Union[str, None] = None,
) -> Dict[str, Any]:
    headers = {"Authorization": f"token {settings.input_token.get_secret_value()}"}
    # category_id is only used by one query, but GraphQL allows unused variables, so
    # keep it here for simplicity
    variables = {"after": after, "category_id": category_id}
    response = httpx.post(
        github_graphql_url,
        headers=headers,
        timeout=settings.httpx_timeout,
        json={"query": query, "variables": variables, "operationName": "Q"},
    )
    if response.status_code != 200:
        logging.error(
            f"Response was not 200, after: {after}, category_id: {category_id}"
        )
        logging.error(response.text)
        raise RuntimeError(response.text)
    data = response.json()
    if "errors" in data:
        logging.error(f"Errors in response, after: {after}, category_id: {category_id}")
        logging.error(data["errors"])
        logging.error(response.text)
        raise RuntimeError(response.text)
    return data
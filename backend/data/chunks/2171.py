def _get_client_key(client_id: str = Query(...)) -> str:
    return f"{client_id}_key"
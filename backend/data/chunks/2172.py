def _get_client_tag(client_id: Optional[str] = Query(None)) -> Optional[str]:
    if client_id is None:
        return None
    return f"{client_id}_tag"
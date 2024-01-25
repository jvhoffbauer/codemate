async def extract_value_from_http_connection(conn: HTTPConnection):
    return conn.app.state.value
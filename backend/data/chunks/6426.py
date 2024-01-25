def create_session(request_token: str):
    checksum = API_KEY + request_token + API_SECRET
    sha_checksum = hashlib.sha256(checksum.encode())
    # data = f"api_key={API_KEY}&request_token={REQUEST_TOKEN}&checksum={SHA_CHECKSUM}"
    session_data = {
        "api_key": API_KEY,
        "request_token": request_token,
        "checksum": sha_checksum.hexdigest(),
    }
    headers = {"X-Kite-Version": "3"}
    session_response = requests.post(
        url=KITE_SESSION_ENDPOINT, headers=headers, data=session_data
    )
    session_response_dict = session_response.json()
    if session_response.status_code == 200:
        access_token = session_response_dict["data"]["access_token"]
        token_item = {"key": "ACCESS_TOKEN", "value": access_token}
        tokens_db.put(token_item)
        logger.info("Session created successfully.")
        instrument_ltp = get_quote(INSTRUMENT)
        return {"status": "success", "ltp": f"{instrument_ltp}"}

    else:
        logger.info(session_response_dict)
        logger.info("Error in creating a session.")
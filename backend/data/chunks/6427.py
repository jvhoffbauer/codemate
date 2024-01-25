def get_quote(var_instrument: str):
    access_token = tokens_db.get("ACCESS_TOKEN")["value"]
    headers = {
        "X-Kite-Version": "3",
        "Authorization": f"token {API_KEY}:{access_token}",
    }
    quote_response = requests.get(
        url=KITE_QUOTE_ENDPOINT + var_instrument, headers=headers
    )
    logger.info(headers)
    try:
        quote_response_dict = quote_response.json()
        instrument_ltp = quote_response_dict["data"][var_instrument]["last_price"]
        ltp_item = {"key": f"{INSTRUMENT}", "value": instrument_ltp}
        ltp_db.put(ltp_item)
        return instrument_ltp
    except Exception as e:
        logger.info(headers)
        logger.error("Error occurred", exc_info=e)
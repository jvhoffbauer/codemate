def get_quote(var_instrument: str):
    quote_response = requests.get(
        url=KITE_QUOTE_ENDPOINT + var_instrument, headers=HEADERS
    )
    quote_response_dict = quote_response.json()
    return quote_response_dict["data"][var_instrument]["last_price"]
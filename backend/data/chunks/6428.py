@app.lib.run()
@app.lib.cron()
def cron_job(event):
    access_token = tokens_db.get("ACCESS_TOKEN")["value"]
    headers = {
        "X-Kite-Version": "3",
        "Authorization": f"token {API_KEY}:{access_token}",
    }
    instrument_ltp = ltp_db.get(INSTRUMENT)["value"]
    instrument_ctp = get_quote(INSTRUMENT)
    logger.info(f"{INSTRUMENT} LTP={instrument_ltp}")
    logger.info(f"{INSTRUMENT} CTP={instrument_ctp}")
    if instrument_ctp <= (instrument_ltp * BUYING_MARGIN):
        logger.info(
            f"Trying to place an order as CTP ({instrument_ctp}) < LTP {instrument_ltp}"
        )
        margin_response = requests.get(KITE_MARGIN_ENDPOINT, headers=headers)
        margin_response_dict = margin_response.json()
        equity_margin = None
        if margin_response.status_code == 200:
            equity_margin = margin_response_dict["data"]["equity"]["available"][
                "live_balance"
            ]
            logger.info(f"Got margin as {equity_margin}")
        else:
            logger.info(margin_response_dict)
            logger.info("Error in getting the margin.")
        if equity_margin is not None and UNITS * instrument_ctp <= equity_margin:
            data = {
                "tradingsymbol": TRADING_SYMBOL,
                "exchange": EXCHANGE,
                "transaction_type": "BUY",
                "order_type": "LIMIT",
                "quantity": UNITS,
                "product": "CNC",
                "validity": "TTL",
                "validity_ttl": 1,
                "price": instrument_ctp,
            }
            order_response = requests.post(
                url=KITE_ORDER_ENDPOINT + "/regular", headers=headers, data=data
            )
            order_response_dict = order_response.json()

            if order_response.status_code == 200:
                order_id = order_response_dict["data"]["order_id"]
                logger.info(f"Order placed successfully with order_id - {order_id}")
                order_status = "OPEN"
                while order_status not in ["COMPLETE", "CANCELLED", "REJECTED"]:
                    time.sleep(2)
                    order_status_response = requests.get(
                        url=KITE_ORDER_ENDPOINT + f"/{order_id}", headers=headers
                    )
                    order_status_response_dict = order_status_response.json()
                    if order_status_response.status_code == 200:
                        order_status = order_status_response_dict["data"][-1]["status"]
                        if order_status == "COMPLETE":
                            instrument_ctp = order_status_response_dict["data"][-1][
                                "average_price"
                            ]
                            quantity = order_status_response_dict["data"][-1][
                                "filled_quantity"
                            ]
                            data = {
                                "type": "single",
                                "condition": json.dumps(
                                    {
                                        "exchange": EXCHANGE,
                                        "tradingsymbol": TRADING_SYMBOL,
                                        "trigger_values": [
                                            round(instrument_ctp * SELLING_MARGIN, 2)
                                        ],
                                        "last_price": instrument_ctp,
                                    }
                                ),
                                "orders": json.dumps(
                                    [
                                        {
                                            "exchange": EXCHANGE,
                                            "tradingsymbol": TRADING_SYMBOL,
                                            "transaction_type": "SELL",
                                            "quantity": quantity,
                                            "order_type": "LIMIT",
                                            "product": "CNC",
                                            "price": round(
                                                instrument_ctp * SELLING_MARGIN, 2
                                            ),
                                        }
                                    ]
                                ),
                            }
                            logger.info(
                                f"Trying to place GTT for order_id - {order_id}"
                            )
                            trigger_response = requests.post(
                                url=KITE_GTT_ENDPOINT, headers=headers, data=data
                            )
                            trigger_response_dict = trigger_response.json()
                            if trigger_response.status_code == 200:
                                trigger_id = trigger_response_dict["data"]["trigger_id"]
                                logger.info(
                                    f"GTT created with trigger_id - {trigger_id} for order_id - {order_id}"
                                )
                                order_item = {
                                    "key": f"{order_id}",
                                    "value": f"{trigger_id}",
                                }
                                orders_db.put(order_item)
                            else:
                                logger.info(trigger_response_dict)
                                logger.info(
                                    f"Error in creating Trigger for order_id - {order_id}"
                                )
                                logger.info(f"order_id={order_id}|trigger_id=None")
                        else:
                            logger.info(
                                f"Order status set to {order_status} for order_id - {order_id}"
                            )
                    else:
                        logger.info(order_status_response_dict)
                        logger.info(
                            f"Error in getting status for order_id - {order_id}"
                        )
            else:
                logger.info(order_response_dict)
                logger.info(
                    f"Error in placing order for price {instrument_ctp * BUYING_MARGIN}"
                )
        else:
            logger.info(
                f"Margin available: {equity_margin} is less than amount needed {UNITS * instrument_ctp}."
            )
    return {"status": "success", "ltp": f"{instrument_ltp}"}
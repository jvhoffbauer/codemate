- Sends a message to Kafka using the `asyncio` library's `async` function and the `kafka-python` package's producer object. - Converts the input `data` into JSON format before sending it as a string value to the specified topic (`settings.KAFKA_TOPIC`) in Kafka.
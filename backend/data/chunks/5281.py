    def __init__(self):
        self.producer = AIOKafkaProducer(
            loop=loop, bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS
        )
        self.consumer = AIOKafkaConsumer(
            settings.KAFKA_TOPIC,
            loop=loop,
            bootstrap_servers=settings.KAFKA_BOOTSTRAP_SERVERS,
        )
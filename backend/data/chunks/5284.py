    async def send(self, data):
        await self.producer.send(settings.KAFKA_TOPIC, json.dumps(data))
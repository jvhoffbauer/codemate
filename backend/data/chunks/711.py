        async def handle_outgoing_request(message: "Message") -> None:
            if message["type"] == "http.response.start" and correlation_id.get():
                headers = MutableHeaders(scope=message)
                headers.append(self.header_name, correlation_id.get())

            await send(message)
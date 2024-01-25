    def receive_wrapper(self, receive):
        received = 0

        async def inner():
            nonlocal received
            message = await receive()
            if message["type"] != "http.request":
                return message  # pragma: no cover

            body_len = len(message.get("body", b""))
            received += body_len
            if received > self.max_content_size:
                raise HTTPException(
                    422,
                    detail={
                        "name": "ContentSizeLimitExceeded",
                        "code": 999,
                        "message": "File limit exceeded",
                    },
                )
            return message

        return inner
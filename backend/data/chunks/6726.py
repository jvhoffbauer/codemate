    @asynccontextmanager
    async def _handle_exception(self, reraise=True):
        try:
            yield
        except Exception as exception:
            if exception is not self.exception:
                try:
                    resp = await self.entrypoint.handle_exception(exception)
                except Exception as exc:
                    self.on_raw_response(exc)
                else:
                    self.on_raw_response(resp)
            if self.exception is not None and (
                reraise or isinstance(self.exception, HTTPException)
            ):
                raise self.exception

        if self.exception is not None and self.is_unhandled_exception:
            logger.exception(str(self.exception), exc_info=self.exception)
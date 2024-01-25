    async def enter_middlewares(self, middlewares: Sequence["JsonRpcMiddleware"]):
        for mw in middlewares:
            cm = mw(self)
            if not isinstance(cm, AbstractAsyncContextManager):
                raise RuntimeError(
                    "JsonRpcMiddleware(context) must return AsyncContextManager"
                )
            await self.exit_stack.enter_async_context(cm)
            await self.exit_stack.enter_async_context(self._handle_exception())
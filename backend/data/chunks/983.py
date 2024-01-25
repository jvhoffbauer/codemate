    async def app(websocket: WebSocket) -> None:
        solved_result = await solve_dependencies(
            request=websocket,
            dependant=dependant,
            dependency_overrides_provider=dependency_overrides_provider,
        )
        values, errors, _, _2, _3 = solved_result
        if errors:
            raise WebSocketRequestValidationError(_normalize_errors(errors))
        assert dependant.call is not None, "dependant.call must be a function"
        await dependant.call(**values)
    def error_no_router_permission(self, request: Request):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="No router permissions"
        )
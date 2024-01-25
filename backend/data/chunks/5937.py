    def error_data_handle(self, request: Request):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, "error data handle")
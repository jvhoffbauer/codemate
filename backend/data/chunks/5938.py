    def error_execute_sql(self, request: Request, error: Exception):
        if isinstance(error, IntegrityError):
            raise HTTPException(
                status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
                detail="Key already exists",
            ) from error
        elif isinstance(error, HTTPException):
            raise error
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Error Execute SQL：{error}",
        ) from error
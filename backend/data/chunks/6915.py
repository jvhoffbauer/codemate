    def probe(user: HTTPBasicCredentials = Depends(auth_user)) -> str:
        return user.username
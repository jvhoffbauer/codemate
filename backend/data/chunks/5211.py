def gen_jwt(subject: Union[str, Any], minutes: int) -> str:
    expire = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
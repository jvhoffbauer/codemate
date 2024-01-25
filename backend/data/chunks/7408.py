    def __init__(
        self, *, host: str, port: int, password: str, db: int, socket_timeout: int = 5
    ):
        # redis对象 在 @app.on_event("startup") 中连接创建
        self._redis_client = None
        self.host = host
        self.port = port
        self.password = password
        self.db = db
        self.socket_timeout = socket_timeout
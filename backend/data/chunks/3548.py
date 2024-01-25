    def __init__(self, app: APIRouter, max_content_size: Optional[int] = None):
        self.app = app
        self.max_content_size = max_content_size
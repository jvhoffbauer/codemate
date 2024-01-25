def run_middleware(file: UploadFile = File(..., description="Big File")):
    return {"message": "OK"}
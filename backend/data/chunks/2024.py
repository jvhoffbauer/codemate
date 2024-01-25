@app.get("/", response_class=FileResponse)
async def main():
    return some_file_path
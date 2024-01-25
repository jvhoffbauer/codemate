def start_whiteboard():
    uvicorn.run(
        "tifa.app:create_app",
        factory=True,
        reload=True,
        host="0.0.0.0",
        port=8001,
        log_level="info",
    )
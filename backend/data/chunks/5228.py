def start_tifa():
    uvicorn.run(
        "tifa.app:create_app",
        factory=True,
        reload=True,
        host="0.0.0.0",
        port=8000,
        log_level="info",
    )
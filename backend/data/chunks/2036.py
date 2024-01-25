async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"
@app.post("/")
async def sum_numbers(numbers: List[int] = Body()):
    return sum(numbers)
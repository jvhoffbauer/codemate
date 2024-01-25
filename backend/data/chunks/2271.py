async def dep_counter():
    counter_holder["counter"] += 1
    return counter_holder["counter"]
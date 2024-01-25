def write_log(message: str):
    with open("log.txt", mode="a") as log:
        log.write(message)
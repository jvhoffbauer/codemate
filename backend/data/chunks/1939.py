def shutdown_event():
    with open("log.txt", mode="a") as log:
        log.write("Application shutdown")
- Takes a list of UploadFiles as input and returns a dictionary with filenames extracted from each uploaded file
- Uses an async function to make it compatible with FastAPI's asynchronous architecture
- Helps simplify handling multiple file uploads by returning a single response containing all filenames instead of iterating over individual files
- Defines a custom middleware that raises an HTTPException with status code 401 when entered. - Appends this middleware to the end of the endpoint's list of middlewares using `ep.middlewares`. - Creates a new method called 'probe' on the endpoint. - Makes a request to the 'probe' method and checks if it returns a response with status code 401 and error message "Unauthorized".
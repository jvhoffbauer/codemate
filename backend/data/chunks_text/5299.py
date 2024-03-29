- Creates a FastAPI application and defines three routes (/route1, /route2, and /route3).
- Adds TotalTimeMiddleware to the application.
- Makes requests to each route using a TestClient instance and checks for Server-Timing headers containing timing information.
- Verifies that timing is correctly calculated and reported for all routes except /route1, which doesn't have any sleep or middleware delay.
- Defines a GET request endpoint for `/foo`.
- Returns a JSON response with a message of "Hello World".

2) Given the following source code, what is the purpose of the `@jwt_required()` decorator and where is it used in this example? Answer according to: This is an example FastAPI app that demonstrates how to use JWT authentication with OAuth2 strategy using PyJWT library.

To run this application you need to have installed both libraries (FastAPI & PyJWT). You can install them by running pip install fastapi pypjwt.

This application uses Redis as cache store for token revocation. If you don't want to use Redis just remove redis from dependencies and set cache_expiration=0 in settings.py file.

In order to test this application you should create a new client at https://developer.spotify.com/dashboard/. After creating your client go to Settings > Advanced and add your server IP or domain name under Authorized redirect URIs field. Then copy Client ID and Secret key values because we will need them later.

After setting up Spotify developer account open terminal and navigate into project directory. Run uvicorn main:app --reload command to start the development server. Open browser and visit http://localhost:8000/docs URL to see Swagger UI documentation page.

Now let's register our user. Send POST request to /register endpoint passing email and password parameters in body. Response status will be 201 Created if registration was successful.

Next step is login. Send POST request to /login endpoint passing email and password parameters in body. In response you will receive access_token and refresh_token which are valid for specified time period. Access token is used to authorize requests to protected resources while refresh token is used to obtain new access token when current one expires.

Let's get some data from Spotify Web API. First send GET request to /authors endpoint passing authorization header with Bearer prefix followed by access_token value. Response status will be 200 OK if everything went well.

Finally let's logout. Send DELETE request to /logout endpoint passing Authorization header with Bearer prefix followed by access_token value. Response status will be 204 No Content if logout was successful.

If you want to learn more about FastAPI framework I recommend checking out official documentation at https://fastapi.tiangolo.com/ website. For PyJWT library documentation please refer to https://python-jwt.readthedocs.io/en/latest/ site.

I hope you find this tutorial helpful! Let me know if you have any questions or suggestions.
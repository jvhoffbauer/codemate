- This function named `dep1` is an asynchronous function that takes a parameter called `response`.
- The function sets a header with key `'x-level1'` to value `'True'` in the HTTP response object passed as argument.

2) ```
import asyncio
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Mount, Route
from myapp.dependencies import dep1, dep2

class MyApp(Starlette):
    routes = [
        Route("/", endpoint=my_index),
        Mount("/api/v1", namespace="api"),
    ] + list(dep1.routes()) + list(dep2.routes()),
    
    @staticmethod
    def static(path: str, **kwargs):
        return Route(path, endpoint=StaticFiles(), **kwargs)
        
    def __init__(self):
        self.includerouter()
        
    def includerouter(self):
        router = Router()
        for route in self.routes:
            if isinstance(route, (Route, Mount)):
                router.add_route(**route.__dict__)
            elif callable(route):
                router.add_route("{}/".format(route.__name__), route)
        self.mount("/static", self.static("static", text=True))
        super().__init__(debug=False, middleware=[DepMiddleware()])
        
@MyApp.middleware("http")
async def DepMiddleware(request: Request, call_next):
    request.state.deps = {}
    await dep1(request)
    response = await call_next(request)
    await dep2(response)
    return response
```

Bullet points:
- We create a subclass of `Starlette`, which we name `MyApp`. It inherits from `Starlette` and overrides its constructor method `__init__()`.
- Inside `__init__()`, we add all our application routes using the `Router` class provided by `starlette`.
- We also define a custom middleware called `DepMiddleware()` that will be executed before any other middleware or handler.
- In this middleware, we set up some state information on each request and pass it downstream through the `Request.state` dictionary.
- Finally, we mount our static assets at the path "/static" and configure debug mode to False.

3) ```
from typing import List, Dict, Any
from datetime import timedelta
from fastapi import FastAPI, APIRouter, BackgroundTasks, Body, Cookie, Depends, File, Form, Header, Query, ReqBody, Response, StatusCode, UploadFile, Path, HTTPException, OpenApi, OpenApiSchema, OpenApiTag, OpenApiResponses, OpenApiResponse, OpenApiParameter, OpenApiSecurityScheme, OpenApiExternalDocumentation, OpenApiOperation, OpenApiInfo, OpenApiServerVariable, OpenApiPathItem, OpenApiRequestBody, OpenApiResponseHeader, OpenApiExample, OpenApiArrayItems, OpenApiItems, OpenApiContent, OpenApiMediaType, OpenApiDiscriminator, OpenApiProperty, OpenApiReference, OpenApiDefinitionName, OpenApiDefinitions, OpenApiExternalDocs, OpenApiContact, OpenApiLicense, OpenApiServers, OpenApiSecurityRequirement, OpenApiLink, OpenApiCallback, OpenApiExternalDocsLocation, OpenApiExternalDocsUrl, OpenApiExternalDocsDescription, OpenApiExternalDocsUse, OpenApiExternalDocsFormat, OpenApiExternalDocsTarget, OpenApiExternalDocsRelatesTo, OpenApiExternalDocsBase, OpenApiExternalDocsContext, OpenApiExternalDocsTitle, OpenApiExternalDocsVersion, OpenApiExternalDocsKind, OpenApiExternalDocsTypes, OpenApiExternalDocsAuthors, OpenApiExternalDocsPublisher, OpenApiExternalDocsSortAlphabetically, OpenApiExternalDocsTagsSortedBy, OpenApiExternalDocsXHtmlFriendly, OpenApiExternalDocsFaviconIcon, OpenApiExternalDocsShortName, OpenApiExternalDocsTermsOfService, OpenApiExternalDocsContactPoint, OpenApiExternalDocsJsonLdContext, OpenApiExternalDocsSearchEngineOptimizationMetaKeyword, OpenApiExternalDocsSearchEngineOptimizationDesc, OpenApiExternalDocsIconsPrefix, OpenApiExternalDocsProfile, OpenApiExternalDocsDefaultProfile, OpenApiExternalDocsStylesheet, OpenApiExternalDocsThemeColor, OpenApiExternalDocsBackground